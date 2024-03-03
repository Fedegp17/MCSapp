from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('inicio/', views.inicio, name='Inicio'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('hospitales/', views.hospitales, name='Hospitales'),
    path('pacientes/', views.pacientes, name='Pacientes'),
    path('configuracion/', views.configuracion, name='Configuracion'),
    path('aviso-privacidad/', views.aviso_privacidad, name='AvisoPrivacidad'),
    path('about-us', views.about_us, name='Historia'),
]
