# Generated by Django 4.0.2 on 2022-03-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_logginnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='otppass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('newpassword', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
                ('otp', models.IntegerField()),
            ],
        ),
    ]