# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20160111_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='active_character_1',
            field=models.ForeignKey(related_name='_active_character_1', to='game.Character_Stats'),
        ),
        migrations.AlterField(
            model_name='player',
            name='active_character_2',
            field=models.ForeignKey(related_name='_active_character_2', to='game.Character_Stats'),
        ),
        migrations.AlterField(
            model_name='player',
            name='active_character_3',
            field=models.ForeignKey(related_name='_active_character_3', to='game.Character_Stats'),
        ),
        migrations.AlterField(
            model_name='player',
            name='dead_characters',
            field=models.ManyToManyField(related_name='_dead_characters', to='game.Character_Stats', blank=True),
        ),
    ]
