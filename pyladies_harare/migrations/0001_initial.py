# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 14:48
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='full name')),
                ('phone', models.CharField(max_length=30, verbose_name='phone number')),
                ('email', models.CharField(max_length=120, verbose_name='email address')),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('emaildate', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fromdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='from date')),
                ('todate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='to date')),
                ('location', models.CharField(max_length=200)),
                ('website', models.TextField()),
                ('comments', models.TextField()),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date posted')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('ispast', models.BooleanField(default=True)),
                ('isdisplayed', models.BooleanField(default=False)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]