# Generated by Django 3.2.5 on 2021-07-23 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_auto_20210723_1510'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
