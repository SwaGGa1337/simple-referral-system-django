# Generated by Django 5.0.3 on 2024-04-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0009_alter_referral_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]