# Generated by Django 4.1.2 on 2022-10-12 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_candidate_dob_alter_usermaster_is_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 12, 23, 59, 57, 21662)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 12, 23, 59, 57, 21662)),
        ),
    ]