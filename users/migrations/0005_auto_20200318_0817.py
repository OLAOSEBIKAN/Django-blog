# Generated by Django 3.0.4 on 2020-03-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200318_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='place.jpg', upload_to='profile_pics'),
        ),
    ]
