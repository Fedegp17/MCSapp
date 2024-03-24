from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import Paciente
from random import randrange
# from iot_platform.medicalIOT.api_endpoint.models import MedicalMonitor
import json
from django.http.response import JsonResponse


# Create your views here.
def home(request):
    return render(request, "iot_temp/home.html")


def inicio(request):
    return render(request, "iot_temp/inicio.html")


def hospitales(request):
    return render(request, "iot_temp/hospitales.html")


def aviso_privacidad(request):
    return render(request, "iot_temp/AvisoPrivacidad.html")


def about_us(request):
    return render(request, "iot_temp/IoTHistory.html")


class Pacientes(ListView):

    template_name = 'iot_temp/pacientes.html'
    model = Paciente

    context_object_name = 'pacientes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conteo'] = context['pacientes'].count()
        return context


class PacientesForm(CreateView):

    # With this we instruct which HTML the class should render/create
    template_name = 'iot_temp/pacientes_form.html'

    # First we need to import the model 'Paciente' so we can access to the database
    model = Paciente
    fields = ['nombre', 'apellidopaterno', 'apellidomaterno']

    success_url = reverse_lazy('Pacientes')
