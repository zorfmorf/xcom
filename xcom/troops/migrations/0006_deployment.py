# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0005_auto_20141218_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('mission', models.ForeignKey(to='troops.Mission')),
                ('soldier', models.ForeignKey(to='troops.Soldier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
