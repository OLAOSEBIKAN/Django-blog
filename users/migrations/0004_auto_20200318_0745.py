# Generated by Django 3.0.4 on 2020-03-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200318_0717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='20200226_144436.jpg', upload_to='display_pic'),
        ),
    ]
