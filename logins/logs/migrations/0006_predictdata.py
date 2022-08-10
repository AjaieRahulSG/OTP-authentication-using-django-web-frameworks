# Generated by Django 4.0.2 on 2022-03-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_alter_otppass_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='predictdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fever', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('breatheproblem', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('drycough', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('sorethroat', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('hypertension', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('abroadtravel', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('contact', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('publicplaceexposed', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('headache', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('lungspain', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('vaccine', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
                ('boosterdose', models.CharField(choices=[('1', 'YES'), ('0', 'NO')], max_length=10)),
            ],
        ),
    ]
