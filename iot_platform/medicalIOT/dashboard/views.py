from django.shortcuts import render
from random import randrange
# from iot_platform.medicalIOT.api_endpoint.models import MedicalMonitor
from django.http.response import JsonResponse
from api_endpoint.models import MedicalMonitor, BeatsPerMinute
from django.views.generic import DetailView


# Create your views here.
def dashboard(request):
    """We can retrieve the firs() and last() object of a mode, but since our model is already sorted by the latest
       created (see our models.py) then in this case we need to retrieve the first() so we have the most recent object"""
    signos = MedicalMonitor.objects.first()
    beats = BeatsPerMinute.objects.first()
    return render(request, "dashboard/dashboard.html", {"signos": signos, "beats": beats})


