# Generated by Django 3.2.3 on 2021-06-10 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitie',
            name='num_members',
            field=models.IntegerField(default=0),
        ),
    ]
