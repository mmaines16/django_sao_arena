from rest_framework import serializers as rest_serializers
from rest_framework.serializers import ModelSerializer
from .models import Active_Effect, Blocked_Skill, Character_Stats, Game, Player

class Active_EffectSerializer(ModelSerializer):
    class Meta:
        model = Active_Effect
        fields = (
            'id',
            'effect',
            'turns_left',
        )

class Blocked_SkillSerializer(ModelSerializer):
    class Meta:
        model = Blocked_Skill
        fields = (
            'id',
            'skill',
            'turns_left',
        )
        
class Character_StatsSerializer(ModelSerializer):
    class Meta:
        model = Character_Stats
        fields = (
            'id',
            'character',
            'health',
            'damage_reduction',
            'destructable_defense',
            'effect_rack',
            'available_skills',
            'cooling_skills',
            'stuned_skills',
        )

class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'game_key',
            'player_1',
            'player_2',
            'is_active',
        )
        
class PlayerSerializer(ModelSerializer):
    active_character_1 = Character_StatsSerializer()
    active_character_2 = Character_StatsSerializer()
    active_character_3 = Character_StatsSerializer()
    
    class Meta:
        model = Player
        fields = (
            'id',
            'player_profile',
            'active_character_1',
            'active_character_2',
            'active_character_3',
            'dead_characters',
            'is_turn',
        )
