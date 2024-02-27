from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('inicio/', views.inicio, name='Inicio'),
    path('/dashboard', views.dashboard, name='Dashboard'),
    path('/hospitales', views.hospitales, name='Hospitales'),
    path('/pacientes', views.pacientes, name='Pacientes'),
    path('/configuracion', views.configuracion, name='Configuracion'),
]
