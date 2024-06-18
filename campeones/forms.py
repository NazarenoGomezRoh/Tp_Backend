from django import forms

from campeones.models import Campeon, User

# def validate_number(value):
#     if not isinstance(value, int):
#         raise ValidationError("El numero debe ser un número entero.")
#     if value > -1:
#         raise ValidationError("El año de aparición debe tener exactamente 4 dígitos.")

class CampeonForm(forms.ModelForm):
    
    # name = forms.CharField(label=False,
    #                        widget=forms.TextInput(attrs={'placeholder': 'Funko name'}))
    # number = forms.IntegerField(label=False,
    #                             widget=forms.TextInput(attrs={'placeholder': 'Funko number'}),
    #                             validators=[validate_number])
    # collection = forms.CharField(label=False,
    #                              widget=forms.TextInput(attrs={'placeholder': 'Funko collection'}))

    class Meta:
        model = Campeon
        fields = [
            'nombre',
            'region',
            'edad',
            'es_mago',
        ]
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'nombre',
            'campeones',
        ]