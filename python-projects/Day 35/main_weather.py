import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Xxz1VZWigewGXrcviZ9bhVN0LwKgLB7G
# SKcc874e9439c4001180df6f23473b87d6
# Twilio Account SID and Auth Token
SID = "ACa6da687c16659fa0393e1893af03199c"
AUTH = "5ca10aa07e8247260099862da820d081"

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = api_key

parameters = {
    "lat": 26.0667,
    "lon": 50.5577,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY
}
# +1 909 403 4209
response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
print(data["hourly"])
weather_slice = data["hourly"][:12]
print(weather_slice)
will_rain = False
for weather in weather_slice:
    weather_code = int(data["hourly"][0]["weather"][0]["id"])
    if weather_code <= 700:
        will_rain = True
        break
if will_rain:
    client = Client(SID, AUTH)
    message = client.messages.create(
        body="It's going to rain today!",
        from_="+1909403 4209",
        to="+97336446029"
    )


print(message.status)
