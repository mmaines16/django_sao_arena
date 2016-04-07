# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20160113_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.ForeignKey(blank=True, to='game.Game', null=True),
        ),
    ]
