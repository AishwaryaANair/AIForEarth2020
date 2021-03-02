from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#Home view

def home(request):
    
    return render(request,'index.html')
# Create your views here.
def index(request):
    return render(request,"index.html")