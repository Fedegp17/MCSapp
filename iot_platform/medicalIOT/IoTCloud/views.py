from django.shortcuts import render


# Create your views here.
def vista(request):
    return render(request, "iot_temp/home.html")
