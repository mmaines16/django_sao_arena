from django.db import models
from arena.models import Character, Effect, Energy, Skill, PlayerProfile

import random

# Create your Game models here.
class Active_Effect(models.Model):
    effect = models.ForeignKey(Effect, blank=False, null=False)
    turns_left = models.IntegerField(null=False, blank=False, default=1)
    
    def __unicode__(self):
        return self.effect.name

    
class Blocked_Skill(models.Model):
    skill = models.ForeignKey(Skill, blank=False, null=False)
    turns_left = models.IntegerField(null=False, blank=False, default=1)
    
    def __unicode__(self):
        return self.skill.name
    
class Character_Stats(models.Model):
    character = models.ForeignKey(Character, blank=False, related_name='_character')
    health = models.IntegerField(null=False, blank=False, default=100)
    damage_reduction = models.IntegerField(null=False, blank=False, default=0)
    destructable_defense = models.IntegerField(null=False, blank=False, default=0)
    effect_rack = models.ManyToManyField('Active_Effect', blank=True)
    available_skills = models.ManyToManyField(Skill, blank=True)
    cooling_skills = models.ManyToManyField('Blocked_Skill', blank=True, related_name='_cooling_skills')
    stuned_skills = models.ManyToManyField('Blocked_Skill', blank=True)

    def __unicode__(self):
        return self.character.name   
    
class Game(models.Model):
    game_key = models.CharField(max_length=150, blank=False, null=False)
    player_1 = models.OneToOneField('Player', blank=False, null=False, related_name='player1')
    player_2 = models.OneToOneField('Player', blank=False, null=False, related_name='player2')
    is_active = models.BooleanField(blank=False, null=False, default=True)
    
    def __unicode__(self):
        return str(self.id)
    
class Player(models.Model):
    player_profile = models.OneToOneField(PlayerProfile, blank=False, null=False, related_name='game_player')
    active_character_1 = models.ForeignKey('Character_Stats', blank=False, related_name='_active_character_1')
    active_character_2 = models.ForeignKey('Character_Stats', blank=False, related_name='_active_character_2')
    active_character_3 = models.ForeignKey('Character_Stats', blank=False, related_name='_active_character_3')
    energy_store = models.ManyToManyField(Energy, related_name="_energy_store", blank=True, null=True)
    dead_characters = models.ManyToManyField('Character_Stats', blank=True, related_name='_dead_characters')
    is_turn = models.BooleanField(blank=False, null=False, default=False)
    #game = models.ForeignKey('Game', null=True, blank=True)
    
    def __unicode__(self):
        return self.player_profile.user.username


    