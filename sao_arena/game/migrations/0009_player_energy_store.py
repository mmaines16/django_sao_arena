# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '__first__'),
        ('game', '0008_remove_player_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='energy_store',
            field=models.ManyToManyField(related_name='_energy_store', to='arena.Energy'),
        ),
    ]
