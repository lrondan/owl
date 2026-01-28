from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote, name='quote'),
    path('/<int:proyecto_id>', views.proyectos_destacados, name='proyectos_destacados'),
]