# Generated by Django 3.2.3 on 2021-06-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_auto_20210612_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
