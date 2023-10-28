from django.urls import path
from main import views

urlpatterns = [
    path('', views.testing, name='index'),
    path('emp/', views.employees, name='emp'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/zakaz/', views.zakaz, name='zakaz'),
]