# Generated by Django 3.2.3 on 2021-06-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitie', '0003_communitie_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitie',
            name='image',
        ),
        migrations.AddField(
            model_name='communitie',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]