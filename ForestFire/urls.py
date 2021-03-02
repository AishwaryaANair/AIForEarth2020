from django.urls import path 
from django.conf import settings 
from . import views

urlpatterns = [
    #Home Page URLs 
    path("",views.index,name="index")
]