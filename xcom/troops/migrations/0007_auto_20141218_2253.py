# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0006_deployment'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='days',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deployment',
            name='result',
            field=models.ForeignKey(null=True, to='troops.Status'),
            preserve_default=True,
        ),
    ]
