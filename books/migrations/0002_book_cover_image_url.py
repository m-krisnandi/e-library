# Generated by Django 4.1 on 2024-08-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image_url',
            field=models.URLField(blank=True),
        ),
    ]
