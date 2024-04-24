from django.urls import path
from . import views

urlpatterns = [
    path('authorize/', views.AuthorizationView.as_view(), name='authorize'),
    path('verify-auth-code/', views.VerifyAuthCodeView.as_view(), name='verify-auth-code'),
    # path('referrals/', views.ReferralsView.as_view(), name='referrals'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('auth/', views.phone_number_input, name='auth'),
]