"""medicalIOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""The urlpatterns where we will have the url directory with all the possible paths that our application will have.
   please note that here we have the path /admin which will direct us to the admin section of the backend. Only 
   authorized users can access to the backend admin section. The other path is empty ''. This is because it is 
   redirecting the code to the folder of the app 'IoTCloud' and then to the script 'urls.py', meaning that all the 
   urls are held in that folder in that script. 
   
   Please refer to the app folder 'IoTCloud' to the script 'urls.py' to see the full list of available urls held in that
   directory. Nothing else is need to be done herer currently"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("IoTCloud.urls")),
    path('api/', include("api_endpoint.urls")),
    path('', include("dashboard.urls")),
]
