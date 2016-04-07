from models import PlayerProfile
from django import forms
from django.contrib.auth.models import User


class PlayerProfileForm(forms.ModelForm):
    
    class Meta:
        model = PlayerProfile
        fields = ('avatar', 'character_1', 'character_2', 'character_3', )

    def UpdateCharacters(self, character_1, character_2, character_3):
        self.fields['character_1'].initial = character_1
        self.fields['character_2'].initial = character_2
        self.fields['character_3'].initial = character_3
        
    def validate(self, characters):
        "Check if value consists only of valid emails."

        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)
        
        character_1 = characters[0]
        character_2 = characters[1]
        character_3 = characters[3]
        
        if character_1 == character_2:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        if character_1 == character_3:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        if character_2 == character_3:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        
    def clean_character1(self):
        data = self.cleaned_data['character_1']
        if character_1 == character_2:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        if character_1 == character_3:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        
        return data
    
    def clean_character2(self):
        data = self.cleaned_data['character_1']
        if character_2 == character_1:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        if character_2 == character_3:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        
        return data
    
    def clean_character3(self):
        data = self.cleaned_data['character_1']
        if character_3 == character_1:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        if character_3 == character_2:
            raise forms.ValidationError("Cannot use more than one instance of a character")
        
        return data
        
        
        
class PlayerProfileUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        
    
    