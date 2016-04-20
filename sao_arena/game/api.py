from django.http import Http404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from game.store_settings import DEFAULT_STORE_ID, GAME_STORE_ID, WAITING_PLAYER_LIST_ID, PROFILE_TO_PLAYER_ID
import redis

import json

from serializers import *
from models import Active_Effect, Blocked_Skill, Character_Stats, Game, Player
from arena.models import *

class Active_EffectViewList(generics.ListAPIView):
    queryset = Active_Effect.objects.all()
    serializer_class = Active_EffectSerializer
    
class Active_EffectViewDetail(generics.RetrieveAPIView):
    queryset = Active_Effect.objects.all()
    serializer_class = Active_EffectSerializer
    
class Blocked_SkillViewList(generics.ListAPIView):
    queryset = Blocked_Skill.objects.all()
    serializer_class = Blocked_SkillSerializer
    
class Blocked_SkillViewDetail(generics.RetrieveAPIView):
    queryset = Blocked_Skill.objects.all()
    serializer_class = Blocked_SkillSerializer
    
class Character_StatsViewList(generics.ListAPIView):
    queryset = Character_Stats.objects.all()
    serializer_class = Character_StatsSerializer
    
class Character_StatsViewDetail(generics.RetrieveAPIView):
    queryset = Character_Stats.objects.all()
    serializer_class = Character_StatsSerializer
    
class GameViewList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
class GameViewDetail(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
class PlayerViewList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
class PlayerViewDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
 

class GameNotFound(APIException):
    status_code = 404
    default_detail = 'Game with player query does not exist.'   

@api_view(['GET', 'POST'])
def game_by_player_id(request, pk):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        #games = Game.objects.all()
        try:
            game_store = redis.StrictRedis(host='localhost', port=6379, db=GAME_STORE_ID)
            game_id = game_store.get(str(PlayerProfile.objects.get(id=pk).id))
            game = Game.objects.get(id=game_id)
            serializer = GameSerializer(game, many=False)
            return Response(serializer.data)
        except:
            raise Http404
        
        return Response(status=404)
        
        ######## NO Redis Implementation ######## (Slower)
        #for game in games:
            #if int(pk) == int(game.player_1.player_profile.id):
                #serializer = GameSerializer(game, many=False)
                #return Response(serializer.data)
            #elif int(pk) == int(game.player_2.player_profile.id):
                #serializer = GameSerializer(game, many=False)
                #return Response(serializer.data)
            #else:
                #raise Http404
        
        #return Response(status=404)

    elif request.method == 'POST':
        #serializer = SnippetSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def in_game_details(request, pk):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        try:
            player = Player.objects.get(id=pk);
            
            c1_health= player.active_character_1.health
            c2_health= player.active_character_2.health
            c3_health= player.active_character_3.health
            
            response = "{" + "c1_health: " + c1_health + ", c2_health: " + c2_health + ", c3_health: " + c3_health + "}"
            
            return Response(json.dumps(response));
        except:
            raise Http404
        
        return Response(status=404)


    elif request.method == 'POST':
        #serializer = SnippetSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'POST'])
def end_turn(request, pk):
    """
    End Turn and update player model.
    """
    if request.method == 'GET':
         try:
             player = Player.objects.get(id=pk);
             
             c1_health= player.active_character_1.health
             c2_health= player.active_character_2.health
             c3_health= player.active_character_3.health
             
             player.energy_store.add(Energy.objects.get(id=1))
             
             
             serialized_player = PlayerSerializer(player)
             
             return Response({"player": serialized_player.data});
         except:
             raise Http404
        
         return Response(status=404)


    elif request.method == 'POST':
        message = request.data['message']
        
        return Response({"recieved_message": message})

