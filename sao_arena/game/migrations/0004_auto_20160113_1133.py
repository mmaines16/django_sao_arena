# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20160111_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='game',
        ),
        migrations.AlterField(
            model_name='character_stats',
            name='cooling_skills',
            field=models.ManyToManyField(related_name='_cooling_skills', to='game.Blocked_Skill', blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_1',
            field=models.OneToOneField(related_name='_player_1', to='game.Player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.OneToOneField(related_name='_player_2', to='game.Player'),
        ),
    ]
