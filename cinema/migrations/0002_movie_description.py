# Generated by Django 4.1.5 on 2023-01-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
