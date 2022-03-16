# Generated by Django 3.2.9 on 2022-03-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
