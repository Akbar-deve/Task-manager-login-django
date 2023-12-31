# Generated by Django 4.1.3 on 2023-07-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_delete_nuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
