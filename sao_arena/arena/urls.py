from django.conf.urls import include, url, patterns
from django.conf import settings

from .api import *

urlpatterns = [
    url(r'^actions/$', ActionViewList.as_view(), name='action-list'),
    url(r'^actions/(?P<pk>\d+)/$', ActionViewDetail.as_view(), name='action-detail'),
    url(r'^damage-types/$', Damage_TypeViewList.as_view(), name='damage_type-list'),
    url(r'^damage-types/(?P<pk>\d+)/$', Damage_TypeViewDetail.as_view(), name='damage_type-detail'),
    url(r'^characters/$', CharacterViewList.as_view(), name='character-list'),
    url(r'^characters/(?P<pk>\d+)/$', CharacterViewDetail.as_view(), name='character-detail'),
    url(r'^effects/$', EffectViewList.as_view(), name='effect-list'),
    url(r'^effects/(?P<pk>\d+)/$', EffectViewDetail.as_view(), name='effect-detail'),
    url(r'^energy/$', EnergyViewList.as_view(), name='energy-list'),
    url(r'^energy/(?P<pk>\d+)/$', EnergyViewDetail.as_view(), name='energy-detail'),
    url(r'^missions/$', MissionViewList.as_view(), name='misssion-list'),
    url(r'^missions/(?P<pk>\d+)/$', MissionViewDetail.as_view(), name='mission-detail'),
    url(r'^objectives/$', ObjectiveViewList.as_view(), name='objective-list'),
    url(r'^objectives/(?P<pk>\d+)/$', ObjectiveViewDetail.as_view(), name='objective-detail'),
    url(r'^player-profiles/$', PlayerProfileViewList.as_view(), name='player-profile-list'),
    url(r'^player-profiles/(?P<pk>\d+)/$', PlayerProfileViewDetail.as_view(), name='player-profile-detail'),
    url(r'^skills/$', SkillViewList.as_view(), name='skill-list'),
    url(r'^skills/(?P<pk>\d+)/$', SkillViewDetail.as_view(), name='skill-detail'),
    url(r'^skill-types/$', Skill_TypeViewList.as_view(), name='skill-type-list'),
    url(r'^skill-types/(?P<pk>\d+)/$', Skill_TypeViewDetail.as_view(), name='skill-type-detail'),
    url(r'^targets/$', TargetViewList.as_view(), name='target-list'),
    url(r'^targets/(?P<pk>\d+)/$', TargetViewDetail.as_view(), name='target-detail'),
    url(r'^users/$', UserViewList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+/$)', UserViewDetail.as_view(), name='user-detail'),

    
]