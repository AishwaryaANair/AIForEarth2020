from django.urls import path 
from django.conf import settings 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import include



urlpatterns = [
    #Home Page URLs 
    path('', views.home, name='home'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
