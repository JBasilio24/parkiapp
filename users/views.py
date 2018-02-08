from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import authenticate
from parkin.forms import RegisterForm

def login(request):
    if request.user.is_authenticated():
        return redirect('park:park')

    mensaje = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('park:park')
        else:
            mensaje = 'Revisa tus credenciales'

    template = 'nosotros.html'
    context = {
        'messange': mensaje,
    }
    return render(request, template, context)


@login_required()
def logout(request):
    logout_django(request)
    return redirect('users:login')

def register(request):
    template = "user_register.html"
    f = RegisterForm()
    messages = None
    context = {
        'title': 'Registro de usuarios',
        'form': f,
        'message': messages
    }
    if request.method == 'POST':
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
        messages = 'Usuario creado correctamente'
    return render(request, template, context)