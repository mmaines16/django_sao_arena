# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_player_energy_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='energy_store',
            field=models.ManyToManyField(related_name='_energy_store', null=True, to='arena.Energy', blank=True),
        ),
    ]
