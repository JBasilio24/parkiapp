from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User

class LogInForm(forms.Form):
    Usuario = forms.CharField(max_length=20)
    Contraseña = forms.CharField(max_length=20, widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'rol',
            'speciality',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
            'rol': 'Tipo de usuario',
            'speciality': 'Especialidad',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['specie'].widget.attrs.update({'class': 'form-control', 'id': 'specieID'})
        self.fields['user_question'].widget.attrs.update({'class': 'hidden'})

    class Meta:
        model = Question
        fields = (
            'title',
            'description',
            'user_question',
            'specie',
        )
        labels = {
            'title': 'Título de la consulta: ',
            'description': 'Descripción de la consulta: ',
            'specie': 'Especie',
            'user_question': 'Usuario',
        }
