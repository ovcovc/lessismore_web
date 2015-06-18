# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.TextField(verbose_name=b'description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'created at')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.TextField(verbose_name=b'description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'created at')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.TextField(verbose_name=b'description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'created at')),
                ('is_accepted', models.BooleanField(default=False)),
                ('x_axis', models.FloatField(default=0.0, verbose_name=b'x-axis position')),
                ('y_axis', models.FloatField(default=0.0, verbose_name=b'y-axis position')),
                ('exercises', models.TextField(null=True, verbose_name=b'exercises', blank=True)),
                ('treatments', models.TextField(null=True, verbose_name=b'treatment', blank=True)),
                ('recovery_time', models.TextField(null=True, verbose_name=b'total recovery time', blank=True)),
                ('medication', models.TextField(null=True, verbose_name=b'suggested medication', blank=True)),
            ],
            options={
                'verbose_name': 'Injury',
                'verbose_name_plural': 'Injuries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'original/')),
                ('thumbnail', models.ImageField(upload_to=b'thumbnails/')),
                ('scaled', models.ImageField(upload_to=b'scaled/')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('description', models.TextField(verbose_name=b'description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'created at')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video_file', models.FileField(null=True, upload_to=b'videos/', blank=True)),
                ('video_url', models.URLField(null=True, verbose_name=b'video URL', blank=True)),
                ('tags', models.ManyToManyField(to='injuries.Tag', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(to='injuries.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
