# Generated by Django 4.0.2 on 2022-03-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_otppass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otppass',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
