import requests
from datetime import datetime

LAT = 26.0667
LONG = 50.5577

# API end point is just a url
# API response is a json object
# request is a python module that is used to make http requests to the API
# 100 is the status code for holding on to the request
# 200 is the status code for success
# 300 is the status code for redirect
# 400 is the status code for client error
# 500 is the status code for server error


def is_night():
    time = datetime.now().hour
    parameters = {"lat": LAT,
                  "lng": LONG,
                  "formatted": 0
                  }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset <= time or time <= sunrise:
        return True


def is_iss_passing():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    if response.status_code == 200:
        data_iss = response.json()["iss_position"]
        iss_lat = float(data_iss["latitude"])
        iss_long = float(data_iss["longitude"])
        if LAT - 5 <= iss_lat <= LAT + 5 and LONG - 5 <= iss_long <= LONG + 5:
            return True


if is_night() and is_iss_passing():
    print("It is night and the ISS is passing over the location")


