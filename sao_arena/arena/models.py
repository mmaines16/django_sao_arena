from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


TARGETS = (
    ('Self', 'Self'),
    ('Ally', 'Ally'),
    ('Enemy', 'Enemy'),
)

ACTION_TYPES = (
    ('inc','Increase'),
    ('red','Reduce'),
    ('prev','Prevent'),
    ('ign','Ignore'),
    ('give','Give'),
    ('cntn','Counter Next'),
    ('cnta','Counter All'),
)

ACTION_FIELDS = (
    ('inv','Invulnerability'),
    ('dmg','Damage'),
    ('dmgr','Damage Reduction'),
    ('stn','Stun'),
    ('desd','Destructable Defense'),
    ('cntn','Counter Next'),
    ('cnta','Counter All'),
)

COLORS = (
    ('Green','Green'),
    ('Red','Red'),
    ('Blue','Blue'),
    ('White','White'),
    ('Black','Black'),
)

TIME_PERIODS = (
    ('SAO','Sword Art Online'),
    ('ALO', 'Alfheim Online'),
    ('SAO2', 'New SAO'),
    ('ALO2', 'New Alfheim Online'),
    ('GGO','Gun Gale Online'),
)
    
CHARACTER_TYPES = (
    ('Player', 'Player'),
    ('NPC', 'NPC'),
    ('Monster', 'Monster'),
)

# Create your models here. 
class Action(models.Model):
    action_type             = models.CharField(max_length=50, null=False, blank=False, choices=ACTION_TYPES)
    action_field            = models.CharField(max_length=50, null=False, blank=False, choices=ACTION_FIELDS)
    amount                  = models.IntegerField(null=False, blank=False, default=0)
    affected_skilltypes     = models.ManyToManyField('Skill_Type', blank=True)
    chained_actions         = models.ManyToManyField('Action', blank=True)
    select_skill            = models.ManyToManyField('Skill', blank=True)
    slug                    = models.SlugField(unique=True)
    
    has_skilltype_requirement = models.BooleanField(blank=False, null=False, default=False)
    has_chained_action = models.BooleanField(blank=False, null=False, default=False)
    
    def __unicode__(self):
        return self.slug
    
    
class Damage_Type(models.Model):
    name                  = models.CharField(max_length=50, null=False, blank=False)
    turn_length           = models.IntegerField(null=False, blank=False, default=1)
    amount                = models.IntegerField(null=False, blank=False, default=0)
    targets                = models.ManyToManyField('Target', blank=False)
    secondary_random      = models.BooleanField(blank=False, null=False, default=False)
    slug                  = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.slug
    
class Effect(models.Model):
    name            = models.CharField(max_length=50, null=False, blank=False)
    turn_length     = models.IntegerField(null=False, blank=False, default=1)
    targets         = models.ManyToManyField('Target', blank=False)
    actions         = models.ManyToManyField('Action', blank=False)
    slug            = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.slug
    
# Create your models here.
class Energy(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    color = models.CharField(max_length=20, choices=COLORS, null=False, blank=False)
    amount = models.IntegerField(blank=False, null=False, default=1)
    #description = models.TextField(max_length=300, blank=True, null=True)
    
    
    def __unicode__(self):
        
        return self.name
    
class Skill(models.Model):
    name         = models.CharField(max_length=50, null=False, blank=False)
    description  = models.TextField(max_length=300, null=False, blank=False)
    damage_types = models.ManyToManyField('Damage_Type', null=False, blank=False, related_name='damagetype_set')
    effects      = models.ManyToManyField('Effect', blank=True)
    energy       = models.ManyToManyField('Energy')
    cooldown     = models.IntegerField(null=False, blank=False, default=0)
    skill_types  = models.ManyToManyField('Skill_Type', blank=True)
    image        = models.ImageField(null=False, blank=False, upload_to='img/skills')
    linked_skill = models.ForeignKey('Skill', blank=True, null=True, related_name='linkedskill_set')
    required_skill        = models.ForeignKey('Skill', blank=True, null=True, related_name='requiredskill_set')
    position     = models.IntegerField(null=False, blank=False, default=0)
    
    def __unicode__(self):
        return self.name
    
class Skill_Type(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __unicode__(self):
        return self.name
    
class Character(models.Model):
    
    name                = models.CharField(max_length=50, null=False, blank=False)
    description         = models.TextField(max_length=300, null=False, blank=False)
    image               = models.ImageField(null=False, blank=False, upload_to='img/skills')
    skills              = models.ManyToManyField('Skill')
    linked_character    = models.ForeignKey('Character', blank=True, null=True)
    character_type      = models.CharField(max_length=50, blank=True, null=True, choices=CHARACTER_TYPES)
    time_period         = models.CharField(max_length=50, blank=True, null=True, choices=TIME_PERIODS)
    activating_missions = models.ManyToManyField('Mission', blank=True)
    slug                = models.SlugField(editable=True, unique=True)
    
    def __unicode__(self):
        return self.name
    
class Objective(models.Model): 
    name           = models.CharField(max_length=50, null=False, blank=False)
    description    = models.TextField(max_length=300, null=False, blank=False)
    character      = models.ForeignKey('Character')
    character_type = models.CharField(max_length=50, blank=True, null=True, choices=CHARACTER_TYPES)
    time_period    = models.CharField(max_length=50, blank=True, null=True, choices=TIME_PERIODS)
    wins_against   = models.IntegerField(null=False, blank=False, default=1)
    wins_in_a_row  = models.IntegerField(null=False, blank=False, default=1)
    slug           = models.SlugField(editable=True, unique=False)
    completed      = models.BooleanField(editable=False, default=False) 
    
    def __unicode__(self):
        return self.name
    
class Mission(models.Model):
    name           = models.CharField(max_length=50, null=False, blank=False)
    description    = models.TextField(max_length=300, null=False, blank=False)
    objectives     = models.ManyToManyField('Objective')
    
    def __unicode__(self):
        return self.name
    
    
class PlayerProfile(models.Model):
    user = models.OneToOneField(User, null=False)
    avatar = models.ImageField(null=True, blank=True, upload_to='img/avatars')
    level = models.IntegerField(default=1, null=False)
    wins = models.IntegerField(default=0, null=False)
    defeats = models.IntegerField(default=0, null=False)
    winstreak = models.IntegerField(default=0, null=False)
    character_1 = models.ForeignKey('Character', related_name="+", null=True, blank=True)
    character_2 = models.ForeignKey('Character', related_name="+", null=True, blank=True)
    character_3 = models.ForeignKey('Character', related_name="+", null=True, blank=True)

    def get_characters(self):
        characters = []
        characters.append(self.character_1)
        characters.append(self.character_2)
        characters.append(self.character_3)
        
        return characters 

    def __unicode__(self):
        return self.user.username
    
    
class Target(models.Model):
    target_name         = models.CharField(max_length=50, null=False, blank=False, choices=TARGETS)
    amount              = models.IntegerField(null=False, blank=False, default=1)
    secondary_random    = models.BooleanField(null=False, blank=False, default=False)
    slug                = models.SlugField(unique=True)

    def __unicode__(self):
        return self.slug

def get_characters(self):
        characters = []
        characters.append(self.character_1)
        characters.append(self.character_2)
        characters.append(self.character_3)
        
        return characters 
    
def create_player(sender, instance, created, **kwargs):
    if created:
        player = PlayerProfile.objects.create(user=instance)
        player.username = player.user.username
        player.save()
        
post_save.connect(create_player, sender=User)