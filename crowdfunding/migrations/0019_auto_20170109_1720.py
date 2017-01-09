# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0018_userextendedforfunding_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextendedforfunding',
            name='funding_type',
            field=models.CharField(blank=True, choices=[(b'MR', b'MemberFunding'), (b'GR', b'GroupFunding')], max_length=2),
        ),
        migrations.AlterField(
            model_name='userextendedforfunding',
            name='user_image',
            field=models.ImageField(blank=True, upload_to=b'image/'),
        ),
    ]