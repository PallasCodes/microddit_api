# Generated by Django 3.2.3 on 2021-06-20 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0007_auto_20210620_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='cover_image',
        ),
    ]
