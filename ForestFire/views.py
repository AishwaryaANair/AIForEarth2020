from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#Home view

def home(request):
    return render(request,'homepage.html')

def render_map(request):
    return render(request,"map.html")
# Create your views here.

# Helper function to generate json of lat_long in required format
def createGeoJSON(lat_data, long_data):
    data_json = list()
    counter = 1
    initial_date = dt.datetime(2021, 2, 1)
    for a, b in zip(lat_data, long_data):
        print(counter)
        if counter % 5 == 0:
            # Ibcrease datetime
            initial_date = initial_date + dt.timedelta(days=1)
        data_json.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [b, a]
                },
                "properties": {
                    "date": initial_date.timestamp(),
                    "datestring": str(initial_date.date())
                }
            }
        )

        counter += 1

    file_json = {
        "type": "FeatureCollection",
        "features": data_json
    }
    print("hi")
    with open("map/static/json/created_data.json", "w", encoding="utf-8") as f:
        json.dump(file_json, f)
    print("hello")
    return HttpResponse(file_json)