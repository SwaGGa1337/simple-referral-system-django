# Generated by Django 5.0.3 on 2024-04-23 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0005_referral_ref_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='referred_users',
        ),
    ]
