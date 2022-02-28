import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

appid = os.getenv("APPID")
lat = 48.135124
lon = -11.581981

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get('AUTH_TOKEN')
print(account_sid)
print(auth_token)


parameters = {
    "lat": lat,
    'lon': lon,
    'appid': appid,
    'exclude': 'current,minutely,daily'

}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()


weather_slice = weather_data['hourly'][:20]
will_rain = False
for hour_data in weather_slice:
    condition = hour_data['weather'][0]['id']

    if int(condition) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(body="print your umbrella.", from_='+19625499365', to='+13695829586')

        print(message.status)
