# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20160113_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_profile',
            field=models.OneToOneField(related_name='game_player', to='arena.PlayerProfile'),
        ),
    ]
