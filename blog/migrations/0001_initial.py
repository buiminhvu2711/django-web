# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.TextField(max_length=200)),
                ('hanhtrinh', models.TextField()),
                ('songay', models.TextField()),
                ('ngaydang', models.DateTimeField(auto_now_add=True)),
                ('ngaydi', models.DateTimeField()),
                ('mota', models.TextField()),
            ],
        ),
    ]