# Generated by Django 3.0.4 on 2020-03-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200317_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='place.jpg', upload_to='profile_pics'),
        ),
    ]
