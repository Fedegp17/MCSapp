from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "iot_temp/home.html")


def inicio(request):
    return render(request, "iot_temp/inicio.html")


def dashboard(request):
    return render(request, "iot_temp/dashboard.html")


def hospitales(request):
    return render(request, "iot_temp/hospitales.html")


def pacientes(request):
    return render(request, "iot_temp/pacientes.html")


def configuracion(request):
    return render(request, "iot_temp/configuracion.html")
