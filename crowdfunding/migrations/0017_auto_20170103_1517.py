# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0016_auto_20170103_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='crowdfundingpostproposal',
            name='group_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdfunding.CrowdFundingMemberGroup'),
        ),
        migrations.AlterField(
            model_name='userextendedforfunding',
            name='funding_amout',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='userextendedforfunding',
            name='group_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdfunding.CrowdFundingMemberGroup'),
        ),
    ]
