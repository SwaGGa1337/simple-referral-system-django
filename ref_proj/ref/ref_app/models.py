from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    auth_code = models.CharField(max_length=4, null=True)
    invite_code = models.CharField(max_length=6, blank=True, null=True)
    activated_invite_code = models.CharField(max_length=6, blank=True, null=True)

class Referral(models.Model):
    ref_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by_user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    refcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)