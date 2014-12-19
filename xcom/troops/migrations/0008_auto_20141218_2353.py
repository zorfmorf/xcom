# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0007_auto_20141218_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soldierevent',
            old_name='event',
            new_name='name',
        ),
    ]
