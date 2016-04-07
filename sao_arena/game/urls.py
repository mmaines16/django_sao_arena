from django.conf.urls import include, url, patterns
from django.conf import settings

from .api import *
from .views import join_game_view, home_view

urlpatterns = [
    url(r'^active-effects/$',Active_EffectViewList.as_view(), name='active-effect-list'),
    url(r'^actions/(?P<pk>\d+)/$', Active_EffectViewDetail.as_view(), name='active-effect-detail'),
    url(r'^blocked-skills/$', Blocked_SkillViewList.as_view(), name='blocked-skill-list'),
    url(r'^blocked-skills/(?P<pk>\d+)/$', Blocked_SkillViewDetail.as_view(), name='blocked-skill-detail'),
    url(r'^character-stats/$', Character_StatsViewList.as_view(), name='character-stats-list'),
    url(r'^character-stats/(?P<pk>\d+)/$', Character_StatsViewDetail.as_view(), name='character-stats-detail'),
    url(r'^games/$', GameViewList.as_view(), name='game-list'),
    url(r'^games/(?P<pk>\d+)/$', GameViewDetail.as_view(), name='game-detail'),
    url(r'^games/by-player/(?P<pk>\d+)/$', game_by_player_id, name='game-by-player-id'),
    url(r'^players/$', PlayerViewList.as_view(), name='player-list'),
    url(r'^players/(?P<pk>\d+)/$', PlayerViewDetail.as_view(), name='player-detail'),
    
    url(r'player/update/(?P<pk>\d+)/$', in_game_details, name='player-update'),
]