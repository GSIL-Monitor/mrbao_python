# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-01-02 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_remove_single_interface_single_interface_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modules_interface',
            name='api_response',
        ),
    ]
