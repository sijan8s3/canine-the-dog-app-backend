# Generated by Django 3.2.9 on 2022-03-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMTPSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_port', models.IntegerField(default=587)),
                ('email_host', models.CharField(blank=True, max_length=100, null=True)),
                ('email_host_user', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_host_password', models.CharField(blank=True, help_text='Use the app password not your actual password for the security reason.', max_length=200, null=True)),
            ],
        ),
    ]
