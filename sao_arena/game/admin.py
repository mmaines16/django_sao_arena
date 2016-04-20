from django.contrib import admin
from models import Active_Effect, Blocked_Skill, Character_Stats, Game, Player

# Register your models here.
class Active_EffectAdmin(admin.ModelAdmin):
    class Meta:
        model = Active_Effect
        exclude = ()

class Blocked_SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Blocked_Skill
        exclude = ()
        
class Character_StatsAdmin(admin.ModelAdmin):
    class Meta:
        model = Character_Stats
        exclude = ()
        
class GameAdmin(admin.ModelAdmin):
    class Meta:
        model = Game
        exclude = ()
        
class PlayerAdmin(admin.ModelAdmin):
    class Meta:
        model = Player
        exclude = ()
        
# Register your models here.

admin.site.register(Active_Effect, Active_EffectAdmin)
admin.site.register(Blocked_Skill, Blocked_SkillAdmin)
admin.site.register(Character_Stats, Character_StatsAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
