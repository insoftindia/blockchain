# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0005_crowdfundingpostproposal_voting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crowdfundingpostproposal',
            name='voting',
        ),
        migrations.AddField(
            model_name='crowdfundingproposalvoting',
            name='propoasl_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crowdfunding.CrowdFundingPostProposal'),
        ),
    ]
