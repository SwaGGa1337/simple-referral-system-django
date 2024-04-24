# Generated by Django 5.0.3 on 2024-04-23 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0002_user_auth_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referred_users',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referres', to='ref_app.user'),
        ),
        migrations.DeleteModel(
            name='InviteCodeUsage',
        ),
    ]
