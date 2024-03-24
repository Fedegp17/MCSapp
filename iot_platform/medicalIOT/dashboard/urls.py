from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('get_chart/', views.get_chart, name='get_chart'),
]
