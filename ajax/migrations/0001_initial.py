# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajaxdb',
            fields=[
                ('itemid', models.IntegerField(serialize=False, primary_key=True)),
                ('itemname', models.CharField(max_length=255)),
                ('itemcontent', models.TextField()),
            ],
        ),
    ]
