# Generated by Django 3.2.3 on 2021-06-12 03:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitie', '0002_communitie_num_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myuser', '0003_myuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='communities',
            field=models.ManyToManyField(blank=True, null=True, to='communitie.Communitie'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='added_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
