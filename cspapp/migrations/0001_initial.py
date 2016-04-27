# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_users',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.TextField(null=True)),
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
                ('name', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to='media', blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('department', models.ForeignKey(default=1, to='cspapp.Department')),
                ('developers', models.ForeignKey(blank=True, to='cspapp.All_users', null=True)),
            ],
        ),
    ]
