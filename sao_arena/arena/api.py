from rest_framework import generics
from serializers import *
from .models import Action, Character , Damage_Type, Effect, Energy, Mission, Objective, PlayerProfile, Skill, Skill_Type, Target

class ActionViewList(generics.ListAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    
class ActionViewDetail(generics.RetrieveAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    
class CharacterViewList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
class CharacterViewDetail(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
class Damage_TypeViewList(generics.ListAPIView):
    queryset = Damage_Type.objects.all()
    serializer_class = Damage_TypeSerializer
    
class Damage_TypeViewDetail(generics.RetrieveAPIView):
    queryset = Damage_Type.objects.all()
    serializer_class = Damage_TypeSerializer
    
class EffectViewList(generics.ListAPIView):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer
    
class EffectViewDetail(generics.RetrieveAPIView):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer
    
class EnergyViewList(generics.ListAPIView):
    queryset = Energy.objects.all()
    serializer_class = EnergySerializer
    
class EnergyViewDetail(generics.RetrieveAPIView):
    queryset = Energy.objects.all()
    serializer_class = EnergySerializer
    
class MissionViewList(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    
class MissionViewDetail(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    
class ObjectiveViewList(generics.ListAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer
    
class ObjectiveViewDetail(generics.RetrieveAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer
    
class PlayerProfileViewList(generics.ListAPIView):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
    
class PlayerProfileViewDetail(generics.RetrieveUpdateAPIView):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = PlayerProfileUpdateSerializer

        return serializer_class
    
class SkillViewList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class SkillViewDetail(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class Skill_TypeViewList(generics.ListAPIView):
    queryset = Skill_Type.objects.all()
    serializer_class = Skill_TypeSerializer
    
class Skill_TypeViewDetail(generics.RetrieveAPIView):
    queryset = Skill_Type.objects.all()
    serializer_class = Skill_TypeSerializer
    
class TargetViewList(generics.ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    
class TargetViewDetail(generics.RetrieveAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    
class UserViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
class UserViewDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer