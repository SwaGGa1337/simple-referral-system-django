from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Referral
from .serializer import UserSerializer, ReferralSerializer
import random
import time

class AuthorizationView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        request.session['phone_number'] = phone_number
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=400)
        user, created = User.objects.get_or_create(phone_number=phone_number)
        if created:
            auth_code = str(random.randint(1000, 9999))
            user.auth_code = auth_code
            user.save()
            print(user.auth_code)
            time.sleep(random.randint(1, 2))
            if user.invite_code is None:
                user.invite_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
                user.save()
        else:
            if user.auth_code:
                user.auth_code = None
                auth_code = str(random.randint(1000, 9999))
                user.auth_code = auth_code
                user.save()
                print(user.auth_code)
                time.sleep(random.randint(1, 2))
        return render(request, 'auth_code_form.html', {'phone_number': phone_number})

class VerifyAuthCodeView(APIView):
    def post(self, request):
        phone_number = request.session.get('phone_number')
        request.session['phone_number'] = phone_number
        auth_code_post = request.data.get('auth_code')
        users = User.objects.filter(phone_number=phone_number)
        user = users.first()
        auth_code = user.auth_code
        if auth_code_post == auth_code:
            return redirect('profile')
        else:
            return Response({'error': 'Authentication code is wrong'}, status=400)

class UserProfileView(APIView):
    def get(self, request):
        phone_number = request.session.get('phone_number')

        user = User.objects.filter(phone_number=phone_number).first()
        serializer = UserSerializer(user)
        ser_dat = serializer.data

        referrals = Referral.objects.filter(ref_by=user.id)
        serializer = ReferralSerializer(referrals, many=True)
        ref_dat = serializer.data

        if not user.activated_invite_code:
            return render(request, 'profile.html', {'ser_dat': ser_dat, 'ref_dat': ref_dat})

        return render(request, 'profile_with_ref.html', {'ser_dat': ser_dat, 'ref_dat': ref_dat})

    def post(self, request):
        phone_number = request.session.get('phone_number')
        # request.session['phone_number'] = phone_number
        user = User.objects.filter(phone_number=phone_number).first()
        if user.activated_invite_code is None:
            invite_code = request.data.get('invite_code')
            refuser = User.objects.filter(invite_code=invite_code).first()
            print(refuser)
            if refuser:
                if refuser.invite_code is not None:
                    refuser_invite_code = refuser.invite_code
                    if invite_code == refuser_invite_code:
                        user.activated_invite_code = invite_code
                        user.save()
                        ref_row = Referral.objects.create(ref_by=refuser, user=user, refcode=invite_code, phone=phone_number)
                        ref_row.save()
                        return redirect('profile')
                        # return render(request, 'profile_with_ref.html', {'phone_number': phone_number})
                else:
                    return Response('Code not valid', status=400)

            else:
                return Response('Code not valid', status=400)

        return render(request, 'profile.html')

def index_view(request):
    return render(request, 'index.html')

def phone_number_input(request):
    return render(request, 'phone_number_form.html')

def profile_show(request):
    return render(request, 'profile.html')
