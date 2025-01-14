# Generated by Django 5.0.1 on 2024-05-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=13)),
                ('category', models.CharField(max_length=50)),
                ('availability_status', models.BooleanField(default=True)),
                ('borrower_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
