# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-17 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0022_auto_20170207_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextendedforfunding',
            name='ether_account_private_key',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
