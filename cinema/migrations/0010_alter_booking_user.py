# Generated by Django 4.1.7 on 2023-05-08 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0009_merge_0004_booking_user_0008_booking_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
