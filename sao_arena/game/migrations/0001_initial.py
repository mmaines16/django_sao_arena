# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_Effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turns_left', models.IntegerField(default=1)),
                ('effect', models.ForeignKey(to='arena.Effect')),
            ],
        ),
        migrations.CreateModel(
            name='Blocked_Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turns_left', models.IntegerField(default=1)),
                ('skill', models.ForeignKey(to='arena.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Character_Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health', models.IntegerField(default=100)),
                ('damage_reduction', models.IntegerField(default=0)),
                ('destructable_defense', models.IntegerField(default=0)),
                ('available_skills', models.ManyToManyField(to='arena.Skill', blank=True)),
                ('character', models.ForeignKey(to='arena.Character')),
                ('cooling_skills', models.ManyToManyField(related_name='cooling_skills', to='game.Blocked_Skill', blank=True)),
                ('effect_rack', models.ManyToManyField(to='game.Active_Effect', blank=True)),
                ('stuned_skills', models.ManyToManyField(to='game.Blocked_Skill', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_key', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_turn', models.BooleanField(default=False)),
                ('active_character_1', models.ForeignKey(related_name='active_character_1', to='game.Character_Stats')),
                ('active_character_2', models.ForeignKey(related_name='active_character_2', to='game.Character_Stats')),
                ('active_character_3', models.ForeignKey(related_name='active_character_3', to='game.Character_Stats')),
                ('dead_characters', models.ManyToManyField(related_name='dead_characters', to='game.Character_Stats', blank=True)),
                ('game', models.ForeignKey(blank=True, to='game.Game', null=True)),
                ('player_profile', models.OneToOneField(to='arena.PlayerProfile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player_1',
            field=models.OneToOneField(related_name='player_1', to='game.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='player_2',
            field=models.OneToOneField(related_name='player_2', to='game.Player'),
        ),
    ]
