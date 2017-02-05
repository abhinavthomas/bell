# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('b1', models.TimeField(blank=True, null=True)),
                ('b2', models.TimeField(blank=True, null=True)),
                ('b3', models.TimeField(blank=True, null=True)),
                ('b4', models.TimeField(blank=True, null=True)),
                ('b5', models.TimeField(blank=True, null=True)),
                ('b6', models.TimeField(blank=True, null=True)),
                ('b7', models.TimeField(blank=True, null=True)),
                ('b8', models.TimeField(blank=True, null=True)),
                ('b9', models.TimeField(blank=True, null=True)),
                ('b10', models.TimeField(blank=True, null=True)),
                ('b11', models.TimeField(blank=True, null=True)),
                ('b12', models.TimeField(blank=True, null=True)),
                ('b13', models.TimeField(blank=True, null=True)),
                ('b14', models.TimeField(blank=True, null=True)),
                ('b15', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='current',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
