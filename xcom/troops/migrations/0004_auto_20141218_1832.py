# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0003_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='squad',
            field=models.ForeignKey(blank=True, to='troops.Squad'),
            preserve_default=True,
        ),
    ]
