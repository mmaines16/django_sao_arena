from django.shortcuts import render, redirect
from .tasks import *
from game.store_settings import DEFAULT_STORE_ID, GAME_STORE_ID, WAITING_PLAYER_LIST_ID
import redis
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from arena.models import *
from django.http import Http404

# Create your views here.
@login_required(login_url='/accounts/login/')
@csrf_protect
def home_view(request):
    player = PlayerProfile.objects.get(user=User.objects.get(username=request.user.username))
    
    if GetCurrentGame(player):
        return game_start_view(request, player.id)
    
    characters = Character.objects.all();
    
    join_url = 'http://localhost:8000/game/join/' + str(player.id) + "/"
    start_url = 'http://localhost:8000/game/start/' + str(player.id) + "/"
    return render(request, 'game_setup.html', {'join_url': join_url, 'start_url': start_url,'player': player, 'characters': characters})

@csrf_protect
def join_game_view(request, pk):
    profile_pk = pk
    
    if(request.method=='GET'):
        return redirect(home_view)
    elif(request.method=='POST'):
        AddToGameWaitList.delay(profile_pk)
        return JsonResponse({'Method':'POST'})

@csrf_protect
def game_view(request, player_id):
    return render(request, 'game_setup.html', {'player_id': player_id})

@csrf_protect
def game_start_view(request, pk):
    
    player_profile = PlayerProfile.objects.get(pk=pk)
    player_id = player_profile.id
    
    try:
        game_store = redis.StrictRedis(host='localhost', port=6379, db=GAME_STORE_ID)
        game_id = game_store.get(str(PlayerProfile.objects.get(id=pk).id))
        game = Game.objects.get(id=game_id)
    except:
        raise Http404
    
    
    if player_profile.id == game.player_1.player_profile.id:
        player = game.player_1
        opponent = game.player_2
    elif player_profile.id == game.player_2.player_profile.id:
        player = game.player_2
        opponent = game.player_1
    else:
        player = game.player_1
        opponent = game.player_2
        
    character1 = player.active_character_1.character
    character2 = player.active_character_2.character
    character3 = player.active_character_3.character
    
    
    skills1 = character1.skills.all()
    skills2 = character2.skills.all()
    skills3 = character3.skills.all()
    
    opp_char1 = opponent.active_character_1.character
    opp_char2 = opponent.active_character_2.character
    opp_char3 = opponent.active_character_3.character
    
    opp_skills1 = opp_char1.skills.all()
    opp_skills2 = opp_char2.skills.all()
    opp_skills3 = opp_char3.skills.all()
    
    updateUrl = "localhost:8000/api/game/players/" + str(player.id) + "/" 
    lookup_id = player.id
    
    
    return render(request, 'index.html', {'player_id': player_id, 'game_id': game_id, 'player':player,
                                          'character1':character1, 'character2':character2, 'character3':character3,
                                          'skills1':skills1, 'skills2':skills2, 'skills3':skills3,
                                          'opp_char1': opp_char1, 'opp_char2': opp_char2, 'opp_char3': opp_char3,
                                          'opp_skills1': opp_skills1, 'opp_skills2': opp_skills2,
                                          'opp_skills3': opp_skills3, 'lookup_id': lookup_id})
