# locations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_location, name='add_location'),
    path("home/",views.home, name="home"),
]
