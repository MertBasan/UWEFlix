# Generated by Django 4.1.7 on 2023-04-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_showing_covid_alter_showing_film_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='covid',
            field=models.BooleanField(),
        ),
    ]