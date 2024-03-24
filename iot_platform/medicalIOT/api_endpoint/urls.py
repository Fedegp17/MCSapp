from django.urls import path
from . import views

urlpatterns = [
    path('mcs-endpoint', views.save_payload, name='save_payload'),
]
