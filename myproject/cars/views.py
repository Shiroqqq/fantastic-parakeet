from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CarForm
from .models import Car

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user  # Привязываем объект к текущему пользователю
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

@login_required
def car_list(request):
    cars = Car.objects.filter(user=request.user)  # Показываем только автомобили текущего пользователя
    return render(request, 'cars/car_list.html', {'cars': cars})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('car_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


