# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import cspapp.models
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('statement', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='All_users',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.TextField()),
                ('body', models.TextField()),
                ('project', models.IntegerField(verbose_name=cspapp.models.Project)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('cap_dep', models.ForeignKey(blank=True, to='cspapp.All_users', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to='media', blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('department', models.ForeignKey(default=1, to='cspapp.Department')),
                ('developers', models.ForeignKey(blank=True, to='cspapp.All_users', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name='Rating (stars)', choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cspapp.Answer')),
                ('creator', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('cspapp.answer',),
        ),
        migrations.CreateModel(
            name='ProjectActivity',
            fields=[
                ('activity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cspapp.Activity')),
                ('creator', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='cspapp.Project')),
            ],
            bases=('cspapp.activity',),
        ),
        migrations.CreateModel(
            name='ProjectReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cspapp.Review')),
                ('project', models.ForeignKey(to='cspapp.Project')),
            ],
            bases=('cspapp.review',),
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('request_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cspapp.Request')),
                ('date', models.DateField(default=datetime.date.today)),
                ('creator', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('cspapp.request',),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activityanswer',
            name='project',
            field=models.ForeignKey(to='cspapp.Activity'),
        ),
    ]
