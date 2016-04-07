# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20160113_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_1',
            field=models.OneToOneField(related_name='player1', to='game.Player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.OneToOneField(related_name='player2', to='game.Player'),
        ),
    ]
