# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mission',
            name='date',
            field=models.DateField(verbose_name='Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='joined',
            field=models.DateField(verbose_name='Joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='soldierevent',
            name='date',
            field=models.DateField(verbose_name='Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='squad',
            name='joined',
            field=models.DateField(verbose_name='Established'),
            preserve_default=True,
        ),
    ]
