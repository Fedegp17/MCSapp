from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import Paciente
from random import randrange
import json
from django.http.response import JsonResponse


# Create your views here.
def home(request):
    return render(request, "iot_temp/home.html")


def inicio(request):
    return render(request, "iot_temp/inicio.html")


def dashboard(request):
    return render(request, "iot_temp/dashboard.html")


def hospitales(request):
    return render(request, "iot_temp/hospitales.html")


# I will use this view to test data reception
def configuracion(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        return JsonResponse(received_data)


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


# Estructura de datos Json para construir gráfico
def get_chart(request):
    # colors = ['blue', 'black', 'yellow', 'orange', 'magenta', 'purple', 'red', 'purple']
    # random_color=colors[randrange(0, len(colors-1))]

    serie = []
    counter = 0

    while counter < 24:
        serie.append(randrange(60, 100))
        counter += 1

    chart = {
        'tooltip': {
            'show': True,
            'trigger': "axis",
            'triggerOn': "mousemove|click"
        },

        'xAxis': [
            {
                # category puede ser texto
                'type': "category",
                'data': ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00",
                         "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
                         "20:00", "21:00", "22:00", "23:00"]

            }
        ],

        'yAxis': [
            {
                # value = números
                'type': "value"
            }
        ],

        'series': [
            {
                'data': serie,
                'type': "line",
                'smooth': "true",
                # 'itemStyle':{
                # 'color': random_color
                # },
                # 'lineStyle':{
                # 'color': random_color
                # }
            }
        ]

    }
    return JsonResponse(chart)
