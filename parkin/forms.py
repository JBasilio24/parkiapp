from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *
from users.models import User

class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['hr'].widget.attrs.update({'class': 'form-control'})
        self.fields['minut'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Car
        fields = (
            'hr',
            'minut',
        )
        labels = {
           'hr': 'Horas',
            'minut': 'Minutos',
        }


class PlatesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlatesForm, self).__init__(*args, **kwargs)
        self.fields['plates'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Car
        fields = (
            'plates',
        )
        labels = {
           'plates': 'Placas',
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'mobil',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
            'mobil': 'Numero de celular',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
