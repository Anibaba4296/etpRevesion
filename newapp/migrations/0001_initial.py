# Generated by Django 5.0.1 on 2024-05-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('profile_picture', models.FileField(upload_to='')),
                ('singnature', models.FileField(upload_to='')),
            ],
        ),
    ]