# Generated by Django 3.2.9 on 2021-12-03 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Image',
            new_name='image',
        ),
    ]
