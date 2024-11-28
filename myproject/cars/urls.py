from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('add/', views.add_car, name='add_car'),  # Страница добавления автомобиля
    path('list/', views.car_list, name='car_list'),  # Список автомобилей

    # Главная страница (переход на список автомобилей)
    path('', views.car_list, name='home'),  # Главная страница ведет на список автомобилей
]