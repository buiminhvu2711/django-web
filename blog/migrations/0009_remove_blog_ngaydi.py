# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171201_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='ngaydi',
        ),
    ]
