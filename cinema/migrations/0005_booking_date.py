# Generated by Django 4.1.7 on 2023-05-07 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_booking_booking_code_booking_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
