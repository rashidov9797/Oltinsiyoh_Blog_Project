# Generated by Django 3.2.3 on 2021-07-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0015_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
