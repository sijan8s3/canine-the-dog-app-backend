# Generated by Django 3.2.9 on 2022-03-18 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
    ]
