from rest_framework import viewsets
from .serializer import BeatsSerializer
from .models import BeatsPerMinute
from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import BeatsPerMinute,MedicalMonitor
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
# The CSRF exempt is needed so our server can admit incoming Json payloads, however, we need security measures
@csrf_exempt
def save_payload(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        # If the payload comes from the PulseOximeter, we save it in this Model
        if payload['dispositivo'] == "PulseOximeter":
            # First we store the Json content in a variable
            latidos = float(payload['beats'])
            # Now we pass the saved data to our model (DataBase)
            registro = BeatsPerMinute.objects.create(
                beats=latidos,
            )

        # Elif if the payload comes from the Medical monitor detector, we save it in this Model
        elif payload['dispositivo'] == "MonitorMedico":
            # First we store the Json content in variables
            nombre = str(payload['paciente'])
            heart_rate_json = float(payload['ritmo_cardiaco'])
            spo2_json = float(payload['spo2'])
            respiracion_json = float(payload['respiracion'])
            presion_sistolica_json = float(payload['presion_sistolica'])
            presion_diastolica_json = float(payload['presion_diastolica'])
            # Now we pass the saved data to our model (DataBase)
            registro = MedicalMonitor.objects.create(
                nombre=nombre,
                heart_rate=heart_rate_json,
                spo2=spo2_json,
                respiracion=respiracion_json,
                presion_sistolica=presion_sistolica_json,
                presion_diastolica=presion_diastolica_json,

            )
        # For any other Json incoming, we don't save it
        else:
            return HttpResponse('Failure to save Json')
    return HttpResponse('Json payload has been saved')
