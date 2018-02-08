from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import CreateView
from .forms import CarForm, PlatesForm
from .models import Car, Terminal, Supervisor, Zone

@login_required()
def park(request):
    supervisor = Supervisor.objects.filter(user=request.user.pk).first()
    car = Car.objects.filter(user=request.user.pk)
    if supervisor:
            template = 'park.html'
            car_terminal = Car.objects.all()
            context = {
                'cars': car_terminal,
            }
    else:
        if car:
            template = 'park.html'
            context = {
                'cars': car,
            }
        else:
            template = 'register_car.html'
            form = PlatesForm(request.POST or None)
            if request.method == 'POST':
                plate = request.POST.get('plates')
                Car.objects.create(user=request.user, plates=plate,)
                return redirect('park:park')
            context = {
                'form': form
            }
    return render(request, template, context)

@login_required()
def change_state(request, idt):
    car = Car.objects.get(user=request.user.pk)
    if car.status == 'FR':
        form = CarForm(request.POST or None)
        messagge = ''
        minut = 0
        if request.method == 'POST':
            car.terminal = Terminal.objects.get(id=idt)
            car.date_start = datetime.now()
            if int(request.POST.get('hr')) > 6:
                messagge = 'Ingresa menores horas'
            elif int(request.POST.get('hr')) == 0 and int(request.POST.get('minut')) < 30:
                messagge = 'El minimo es de 30 minutos'
            else:
                hr = int(request.POST.get('hr'))
                minut = int(request.POST.get('minut'))
                hr = hr + int(car.date_start.strftime('%H'))
                minut = minut + int(car.date_start.strftime('%M'))
                print('aqui llega')
                car.hr = hr
                car.minut = minut
                #if car.hr > 24:
                #    messagge = 'No puedes ingresar esas horas'
                if car.minut >= 60:
                    car.hr = car.hr + 1
                    car.minut = car.minut - 60
                car.status = 'OC'
                car.save()
                return redirect('park:park')
        template = 'time.html'
        context = {
            'form': form,
            'message': messagge,
            }
        return render(request, template, context)
    else:
        form = CarForm(request.POST or None)
        messagge = 'Agregue tiempo'
        if request.method == 'POST':
            car.terminal = Terminal.objects.get(id=idt)
            car.date_start = datetime.now()
            if int(request.POST.get('hr')) > 6:
                messagge = 'Ingresa menores horas'
            elif int(request.POST.get('hr')) == 0 and int(request.POST.get('minut')) < 30:
                messagge = 'El minimo es de 30 minutos'
            else:
                hr = car.hr
                minut = car.minut
                hr = hr + int(car.date_start.strftime('%H'))
                minut = minut + int(car.date_start.strftime('%M'))
                print('aqui llega')
                car.hr = hr
                car.minut = minut
                # if car.hr > 24:
                #    messagge = 'No puedes ingresar esas horas'
                if car.minut >= 60:
                    car.hr = car.hr + 1
                    car.minut = car.minut - 60
                car.status = 'OC'
                car.save()
                return redirect('park:park')
        template = 'time.html'
        context = {
            'form': form,
            'message': messagge,
        }
        return render(request, template, context)

@login_required()
def close(request):
    car = Car.objects.get(user=request.user.pk)
    car.status = 'FR'
    car.save()
    return redirect('park:park')