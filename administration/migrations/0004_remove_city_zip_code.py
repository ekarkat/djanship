# Generated by Django 5.0.6 on 2024-06-19 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_userprofile_city_userprofile_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='zip_code',
        ),
    ]