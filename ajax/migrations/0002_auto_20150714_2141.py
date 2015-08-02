# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajaxdb',
            name='itemurl',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ajaxdb',
            name='itemcontent',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ajaxdb',
            name='itemname',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
