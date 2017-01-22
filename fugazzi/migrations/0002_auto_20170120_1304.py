# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-20 13:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fugazzi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='movie',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='lang',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='num',
            new_name='number_of_episodes',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='numofepisodes',
            new_name='season_no',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='genre',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='numofseasons',
            new_name='number_of_seasons',
        ),
        migrations.RemoveField(
            model_name='episodes',
            name='viewlink',
        ),
        migrations.RemoveField(
            model_name='links',
            name='downloadable',
        ),
        migrations.RemoveField(
            model_name='links',
            name='quality',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='releaseyear',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='viewlink',
        ),
        migrations.RemoveField(
            model_name='series',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='series',
            name='viewlink',
        ),
        migrations.DeleteModel(
            name='Cast',
        ),
    ]