# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host_app', '0003_auto_20171025_1626'),
        ('musician_app', '0002_auto_20171025_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicians',
            name='show_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='host_app.Shows'),
        ),
    ]
