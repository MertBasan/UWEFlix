# Generated by Django 4.1.5 on 2023-01-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='age_rating',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
