from django.urls import path
from . import views
from .views import PacientesForm, Pacientes

urlpatterns = [
    path('', views.home, name="Home"),
    path('inicio/', views.inicio, name='Inicio'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('hospitales/', views.hospitales, name='Hospitales'),
    path('pacientes/', Pacientes.as_view(), name='Pacientes'),
    path('configuracion/', views.configuracion, name='Configuracion'),
    path('aviso-privacidad/', views.aviso_privacidad, name='AvisoPrivacidad'),
    path('about-us', views.about_us, name='Historia'),
    path('nuevo-paciente/', PacientesForm.as_view(), name='PacienteNuevo')
]
