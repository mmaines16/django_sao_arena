from arena.models import *
from game.models import *
from game.store_settings import DEFAULT_STORE_ID, GAME_STORE_ID, WAITING_PLAYER_LIST_ID, PROFILE_TO_PLAYER_ID

from celery.decorators import task

import redis
from .queues import RedisQueue

@task()
def CreateGame(profile1, profile2):
    
    
    try:
        game_store = redis.StrictRedis(host='localhost', port=6379, db=GAME_STORE_ID)
        player_store = redis.StrictRedis(host='localhost', port=6379, db=PROFILE_TO_PLAYER_ID)
    except:
        print "<<ERROR>> Could not create game"
        return 
        
    
    
    game = Game(game_key='test_key')
    
    
    player1 = Player(player_profile=profile1)
    
    character1= Character_Stats(character=profile1.character_1)
    character2= Character_Stats(character=profile1.character_2)
    character3= Character_Stats(character=profile1.character_3)

    
    character1.save()
    character2.save()
    character3.save()
    
    
    player1.active_character_1= character1
    player1.active_character_2=character2
    player1.active_character_3=character3
    
    player1.active_character_1_id = character1.id
    player1.active_character_2_id = character2.id
    player1.active_character_3_id = character3.id
    
    for skill in player1.active_character_1.character.skills.all():
        player1.active_character_1.available_skills.add(skill)
        
    for skill in player1.active_character_2.character.skills.all():
        player1.active_character_2.available_skills.add(skill)
        
    for skill in player1.active_character_3.character.skills.all():
        player1.active_character_3.available_skills.add(skill)
    
    player1.active_character_1.save()
    player1.active_character_2.save()
    player1.active_character_3.save()
    player1.save()

    player2 = Player(player_profile=profile2)

    character1= Character_Stats(character=profile2.character_1)
    character2= Character_Stats(character=profile2.character_2)
    character3= Character_Stats(character=profile2.character_3)
    
    
    character1.save()
    character2.save()
    character3.save()
    
    
    player2.active_character_1=character1
    player2.active_character_2=character2
    player2.active_character_3=character3
    
    player2.active_character_1_id = character1.id
    player2.active_character_2_id = character2.id
    player2.active_character_3_id = character3.id

    for skill in player2.active_character_1.character.skills.all():
        player2.active_character_1.available_skills.add(skill)
        
    for skill in player2.active_character_2.character.skills.all():
        player2.active_character_2.available_skills.add(skill)
        
    for skill in player2.active_character_3.character.skills.all():
        player2.active_character_3.available_skills.add(skill)

    player2.active_character_1.save()
    player2.active_character_2.save()
    player2.active_character_3.save()
    player2.save()
    
    game.player_1=player1
    game.player_2=player2
    game.is_active = True
    
    game.save()
    
    game.player_1.game = game
    game.player_2.game = game
    
    game.player_1.save()
    game.player_2.save()
    
    game_store.set(str(game.player_1.player_profile.id), str(game.id))
    game_store.set(str(game.player_2.player_profile.id), str(game.id))
    
    player_store.set(str(game.player_1.player_profile.id), str(game.player_1.id))
    player_store.set(str(game.player_2.player_profile.id), str(game.player_2.id))
    
    
    return game


@task()
def CleanGameDB():
    Game.objects.all().delete()
    Player.objects.all().delete()
    Character_Stats.objects.all().delete()
    
    #print 'Games: ' + Game.objects.all()
    #print 'Players: ' + Player.objects.all()
    #print 'Character_Stats: ' + Character_Stats.objects.all()



@task()  
def GetCurrentGame(profile):
    try:
        game_store = redis.StrictRedis(host='localhost', port=6379, db=GAME_STORE_ID)
        game_id = game_store.get(str(profile.id))
        game = Game.objects.get(id=game_id)
        return game
    except:
        print "<<ERROR>> Could not retrieve game"
        return None
    
@task()
def RemoveFromGameStore(profile_id):
    try:
        game_store = redis.StrictRedis(host='localhost', port=6379, db=GAME_STORE_ID)
        game_store.delete(str(profile_id))
        return
    except:
        print "<<ERROR>> Could not remove game from game_store. May not have found ID"
        return None
    
@task()
def RemoveFromPlayerStore(profile_id):
    try:
        player_store = redis.StrictRedis(host='localhost', port=6379, db=PROFILE_TO_PLAYER_ID)
        player_store.delete(str(profile_id))
        return
    except:
        print "<<ERROR>> Could not remove game from game_store. May not have found ID"
        return None
    
@task()
def EndGame(game_id):
    game = Game.objects.get(id=game_id)
    
    RemoveFromGameStore.delay(str(game.player_1.player_profile.id))
    RemoveFromGameStore.delay(str(game.player_2.player_profile.id))
    
    RemoveFromPlayerStore.delay(str(game.player_1.player_profile.id))
    RemoveFromPlayerStore.delay(str(game.player_2.player_profile.id))
    
    game.player_1.active_character_1.delete()
    game.player_1.active_character_2.delete()
    game.player_1.active_character_3.delete()

    game.player_2.active_character_1.delete()
    game.player_2.active_character_2.delete()
    game.player_2.active_character_3.delete()
    
    game.player_1.delete()
    game.player_2.delete()
    
    game.delete()       
    
@task()
def AddToGameWaitList(profile_id):
    
    try:
        game_queue = RedisQueue('wait-queue')
        game_queue.put(str(profile_id))
        
        if game_queue.qsize() > 1:
            MatchPlayers.delay()
    except:
        print "<<ERROR>> Could not add to wait list"
        return
        
    
@task()
def MatchPlayers():
    try:
        game_queue = RedisQueue('wait-queue')
        player_id_1 = game_queue.get()
        player_id_2 = game_queue.get()
        profile1 = PlayerProfile.objects.get(id=player_id_1)
        profile2 = PlayerProfile.objects.get(id=player_id_2)   
    except:
        print "<<ERROR>> Could match players from wait list"
        return
        
    CreateGame.delay(profile1, profile2)
    
    return

########################  In Game Operations ##############################
## Takes in a Character_Stats Model and a damage amount. The function updates the health field,
## then saves the model with its new values
@task() 
def InflictDamage(character_stats, amount):
    character_stats.health = character_stats.health - amount
    character_stats.save()
