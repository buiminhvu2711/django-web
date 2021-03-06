# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171127_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='gia',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='noidung',
            field=models.TextField(verbose_name='Nội dung'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=0.005949429846306396, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.Category'),
            preserve_default=False,
        ),
    ]
