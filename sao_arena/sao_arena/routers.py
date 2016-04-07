from rest_framework import routers

from arena.api import *

router = routers.SimpleRouter()
router.register(r'actions', ActionViewSet)
router.register(r'damage-types', Damage_TypeViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'effects', EffectViewSet)
router.register(r'energy', EnergyViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'objectives', ObjectiveViewSet)
router.register(r'player-profiles', PlayerProfileViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'skill-types', Skill_TypeViewSet)
router.register(r'targets', TargetViewSet)
router.register(r'users', UserViewSet)