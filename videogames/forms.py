from django import forms

from videogames.models import Videogames , User


class VideogamesForm(forms.ModelForm):

    class Meta:
        model = Videogames
        fields = [
            'nombre',
            'anio',
            'genero',
            'es_goty',
        ]
        
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'nombre',
            'videogames',
        ]