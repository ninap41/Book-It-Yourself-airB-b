# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
        ('host_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('other_profiles', models.TextField()),
                ('email', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('musician_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=b'')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.Users')),
                ('venue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_app.Venues')),
            ],
        ),
    ]
