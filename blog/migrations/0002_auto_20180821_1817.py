# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='blog.Comment'),
        ),
    ]
