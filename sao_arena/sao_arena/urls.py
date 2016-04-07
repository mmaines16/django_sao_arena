"""sao_arena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from arena.views import home_view
from arena import views as arena_views
from django.conf import settings

from arena import urls as arena_urls
from game import urls as game_urls
from game.views import join_game_view
from game.views import home_view as game_home_view
from game.views import game_start_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/arena/', include(arena_urls)),
    url(r'^api/game/', include(game_urls)),
    url(r'^$', home_view, name="Home"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^game-manual/characters/$', arena_views.CharacterView, name='characters'),
    url(r'^game-manual/characters/(?P<slug>[\w-]+)$', arena_views.CharacterSkillsView, name='character skills'),
    url(r'^profile$', arena_views.PlayerProfileView, name='Profile'),
    
    url(r'^game/join/(?P<pk>\d+)/$', join_game_view, name='join-game'),
    url(r'^game/join/$', game_home_view, name='join-game-home'),
    
    url(r'^game/start/(?P<pk>\d+)/$', game_start_view, name='join-game'),
]
