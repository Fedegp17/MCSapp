from django.shortcuts import render
from random import randrange
# from iot_platform.medicalIOT.api_endpoint.models import MedicalMonitor
from django.http.response import JsonResponse
import json


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


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

