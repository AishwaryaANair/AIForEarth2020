import requests
import json

def jprint(ob):
    # create a formatted string of the Python JSON object
    text = json.dumps(ob, sort_keys=True, indent=4)
    print(text)


response = requests.get("http://api.worldweatheronline.com/premium/v1/past-weather.ashx?q=Mumbai&format=JSON&extra=&date=2020-02-20&enddate=2020-02-25&includelocation=&key=035c548ee4e04cacb9a144203202502")
print(response.status_code)
jprint(response.json())
