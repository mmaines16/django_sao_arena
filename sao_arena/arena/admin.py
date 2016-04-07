from django.contrib import admin
from models import Action, Character, Damage_Type, Effect, Energy, Mission, Objective, PlayerProfile, Skill, Skill_Type, Target  
from forms import PlayerProfileForm

# Create your models here.
class ActionAdmin(admin.ModelAdmin):
    class Meta:
        model = Action
        exclude = ()
      
    prepopulated_fields = {'slug': ('action_type', 'action_field', 'amount', 'has_chained_action', 'has_skilltype_requirement'), }


class Damage_TypeAdmin(admin.ModelAdmin):
    class Meta:
        model = Damage_Type
        exclude = ('slug')
        
    prepopulated_fields = {'slug': ('name', 'amount', 'turn_length'), }
    
class EffectAdmin(admin.ModelAdmin):
    class Meta:
        model = Effect
        exclude = ('slug')
        
    prepopulated_fields = {'slug': ('name', 'turn_length'), }

class EnergyAdmin(admin.ModelAdmin):
    class Meta:
        model = Energy
        exclude = ()
    
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill
        exclude = ()
        
class Skill_TypeAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill_Type
        exclude = ()
    
class CharacterAdmin(admin.ModelAdmin):
    class Meta:
        model = Character
        exclude = ()
        
    prepopulated_fields = {'slug': ('name',), }
    
class ObjectiveAdmin(admin.ModelAdmin):
    class Meta:
            model = Objective
            exclude = ()
    
class MissionAdmin(admin.ModelAdmin):
    class Meta:
        model = Mission
        exclude = ()
        
class PlayerProfileAdmin(admin.ModelAdmin):
    
    fields = ('user', 'avatar', 'character_1', 'character_2', 'character_3', )
    
    class Meta:
        form = PlayerProfileForm
        
class TargetAdmin(admin.ModelAdmin):
    class Meta:
        model = Target
        exclude = ()
        
    prepopulated_fields = {'slug': ('target_name', 'amount', 'secondary_random'), }

 
# Register your models here.

admin.site.register(Action, ActionAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Damage_Type, Damage_TypeAdmin)
admin.site.register(Effect, EffectAdmin)
admin.site.register(Energy, EnergyAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Skill_Type, Skill_TypeAdmin)
admin.site.register(PlayerProfile, PlayerProfileAdmin)
admin.site.register(Target, TargetAdmin)
