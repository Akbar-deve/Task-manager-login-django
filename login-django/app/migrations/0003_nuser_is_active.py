# Generated by Django 4.1.3 on 2023-07-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_nuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='nuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
