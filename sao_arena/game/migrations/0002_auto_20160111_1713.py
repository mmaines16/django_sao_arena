# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character_stats',
            name='character',
            field=models.ForeignKey(related_name='_character', to='arena.Character'),
        ),
    ]
