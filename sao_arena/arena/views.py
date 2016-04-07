from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from arena.models import Character, PlayerProfile
from arena import forms


# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

# Create your views here.
def CharacterView(request):
    
    c = Character.objects.all()
    

    return render(request, 'characters.html', {'characters': c})

def CharacterSkillsView(request, slug):    
    c = Character.objects.get(slug=slug)
    skills_set = c.skills.all()
    
    return render(request, 'characterskills.html', {'skill_set': skills_set, 'character': c})

@login_required(login_url='/accounts/login/')
@csrf_protect
def PlayerProfileView(request):
    
    if 'recent_change' in request.session:
        recent_change = request.session['recent_change']
    else:
        recent_change = False
        request.session['recent_change'] = False
    
    if 'edit' in request.session:
        editing = request.session['edit']
    else:
        editing = False
    user = User.objects.get(username=request.user.username)
    player = PlayerProfile.objects.get(user=User.objects.get(username=request.user.username))
    
    characters = []
    
    if player:
        characters = player.get_characters()
    
    if 'edit' in request.session:
        session = request.session['edit']
    post = request.POST

    csrf_token = csrf(request)
    
                                                            
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        user_form = forms.PlayerProfileUserForm(request.POST, instance=user)
        player_form = forms.PlayerProfileForm(request.POST, instance=player)
    
        
        if request.POST.get("submit_edit"):
            editing = True
            request.session['edit'] = True
            return render(request, 'PlayerProfile.html', {
                                                            "post": post,
                                                            "session": session,
                                                            "user": request.user,
                                                            "player": player,
                                                            "player_form": player_form,
                                                            "user_form": user_form,
                                                            "characters": characters,
                                                            "editing": editing,
                                                          })
        
        
        
        
        if user_form.is_valid:
            profile = user_form.save(commit=False)
            profile.user = user
            if request.POST.get('first_name', False):
                profile.first_name = request.POST.get('first_name', False)
            else:
                profile.first_name = user.first_name
            if request.POST.get('last_name', False):
                profile.first_name = request.POST.get('last_name', False)
            else:
                profile.last_name = user.last_name
            profile.save()
        if player_form.is_valid:
            profile = player_form.save(commit=False)
            
            if request.POST.get('avatar', False):
                profile.avatar = request.POST.get('avatar', False)
            else:
                profile.avatar = player.avatar
            if request.POST.get('character_1', False):
                print request.POST.get('character_1', False)
                profile.character_1 = Character.objects.get(id=request.POST.get('character_1', False))
            else:
                profile.character_1 = characters[0]
            if request.POST.get('character_2', False):
                profile.character_2 = Character.objects.get(id=request.POST.get('character_2', False))
            else:
                profile.character_2 = characters[1]
            if request.POST.get('character_3', False):
                profile.character_3 = Character.objects.get(id=request.POST.get('character_3', False))
            else:
                profile.character_3 = characters[2]
            profile.player = player
            profile.save()
            editing = False
            request.session['edit'] = False
            recent_change = True
            request.session['recent_change'] = True
            
            characters = []
    
            if player:
                characters = player.get_characters()
                
            user_form = forms.PlayerProfileUserForm(instance=user)
            player_form = forms.PlayerProfileForm(instance=player)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        INITIAL_VALUES = {'avatar': player.avatar, 'character_1': characters[0], 'character_2': characters[1], 'character_3': characters[2]}
        
        user_form = forms.PlayerProfileUserForm(instance=user)
        player_form = forms.PlayerProfileForm(instance=player, initial=INITIAL_VALUES)
        
        player_form.UpdateCharacters(characters[0], characters[1], characters[2])
        
        editing = False
        request.session['edit'] = False   
        pass
    
    

    return render(request, 'PlayerProfile.html', {
                                                            "post": post,
                                                            "user": request.user,
                                                            "player": player,
                                                            "player_form": player_form,
                                                            "user_form": user_form,
                                                            "characters": characters,
                                                            "editing": editing,
                                                          })

def ReloadPage(request, context):
    return render(request, 'PlayerProfile.html', context)