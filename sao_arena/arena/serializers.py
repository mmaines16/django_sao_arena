from rest_framework import serializers as rest_serializers
from rest_framework.serializers import ModelSerializer
from .models import Action, Character , Damage_Type, Effect, Energy, Mission, Objective, PlayerProfile, Skill, Skill_Type, Target
#from .serializers import SkillSerializer
from django.contrib.auth.models import User

class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = (
            'id',
            'action_type',
            'action_field',
            'amount',
            'affected_skilltypes',
            'chained_actions',
            'select_skill',
            'slug',
            'has_skilltype_requirement',
            'has_chained_action',
        )

class SkillSerializer(ModelSerializer):
    
    #linked_skill = SkillSerializer()
    
    class Meta:
        model = Skill
        fields = (
            'id',
            'name',
            'description',
            'damage_types',
            'effects',
            'energy',
            'cooldown',
            'skill_types',
            'image',
            'linked_skill',
            'required_skill',
            'position',
        )

class CharacterSerializer(ModelSerializer):
    #skills = SkillSerializer(many=True)
    
    class Meta:
        model = Character
        
        fields = (
            'id',
            'name',
            'description',
            'image',
            'skills',
            'linked_character',
            'character_type',
            'time_period',
            'activating_missions',
            'slug',
        )
        
        

class Damage_TypeSerializer(ModelSerializer):
    class Meta:
        model = Damage_Type
        fields = (
            'id',
            'name',
            'turn_length',
            'amount',
            'targets',
            'secondary_random',
            'slug',
        )

class EffectSerializer(ModelSerializer):
    class Meta:
        model = Effect
        fields = (
            'id',
            'name',
            'turn_length',
            'targets',
            'actions',
            'slug',
        )
        
class EnergySerializer(ModelSerializer):
    class Meta:
        model = Energy
        fields = (
            'id',
            'name',
            'color',
            'amount',
        )
        
class MissionSerializer(ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            'id',
            'name',
            'description',
            'objectives',
        )
        
class ObjectiveSerializer(ModelSerializer):
    class Meta:
        model = Objective
        fields = (
            'id',
            'name',
            'description',
            'character',
            'character_type',
            'time_period',
            'character_type',
            'time_period',
            'wins_against',
            'wins_in_a_row',
            'slug',
            'completed',
        )
        
class PlayerProfileSerializer(ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = (
            'id',
            'user',
            'avatar',
            'level',
            'wins',
            'defeats',
            'winstreak',
            'character_1',
            'character_2',
            'character_3',
        )
        
class PlayerProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = (
            #'avatar',
            #'level',
            #'wins',
            #'defeats',
            #'winstreak',
            'character_1',
            'character_2',
            'character_3',
        )
        
        
class Skill_TypeSerializer(ModelSerializer):
    class Meta:
        model = Skill_Type
        fields = (
            'id',
            'name',
        )
        
class TargetSerializer(ModelSerializer):
    class Meta:
        model = Target
        fields = (
            'id',
            'target_name',
            'amount',
            'secondary_random',
            'slug',
        )
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )