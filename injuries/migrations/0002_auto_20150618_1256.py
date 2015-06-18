# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('injuries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='injury',
            name='is_accepted',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
