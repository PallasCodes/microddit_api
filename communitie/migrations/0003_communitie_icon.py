# Generated by Django 3.2.3 on 2021-06-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitie', '0002_communitie_num_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitie',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
