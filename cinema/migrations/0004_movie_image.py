# Generated by Django 4.1.5 on 2023-01-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_movie_age_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/covers'),
        ),
    ]