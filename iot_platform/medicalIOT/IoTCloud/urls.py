from django.urls import path
from . import views
from .views import PacientesForm, Pacientes

urlpatterns = [
    path('', views.home, name="Home"),
    path('inicio/', views.inicio, name='Inicio'),
    path('hospitales/', views.hospitales, name='Hospitales'),
    path('pacientes/', Pacientes.as_view(), name='Pacientes'),
    path('aviso-privacidad/', views.aviso_privacidad, name='AvisoPrivacidad'),
    path('about-us', views.about_us, name='Historia'),
    path('nuevo-paciente/', PacientesForm.as_view(), name='PacienteNuevo')
]
