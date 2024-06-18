from django import forms

from libros.models import Libros,User


class LibrosForm(forms.ModelForm):

    class Meta:
        model = Libros
        fields = [
            'nombre',
            'autor',
            'genero',
            'es_tapa_dura',
        ]
        
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'nombre',
            'libros',
        ]