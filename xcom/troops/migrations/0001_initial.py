# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('wounded', models.IntegerField(default=0)),
                ('dead', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MissionResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MissionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('joined', models.DateTimeField(verbose_name='Joined')),
                ('rank', models.ForeignKey(to='troops.Rank')),
                ('role', models.ForeignKey(to='troops.Role')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SoldierEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('event', models.CharField(max_length=200)),
                ('soldier', models.ForeignKey(to='troops.Soldier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('joined', models.DateTimeField(verbose_name='Established')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='soldier',
            name='squad',
            field=models.ForeignKey(to='troops.Squad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='soldier',
            name='status',
            field=models.ForeignKey(to='troops.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='missionType',
            field=models.ForeignKey(to='troops.MissionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='result',
            field=models.ForeignKey(to='troops.MissionResult'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mission',
            name='squad',
            field=models.ForeignKey(to='troops.Squad'),
            preserve_default=True,
        ),
    ]
