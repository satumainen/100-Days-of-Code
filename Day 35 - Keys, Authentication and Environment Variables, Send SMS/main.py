"""
API Authentication
- up to this lecture, we have learnt about API endpoints and parameters - API's were free
- in this lecture we learn about APIs that require authentication
- API Key - prevents misuse
    - like your personal account number/password
    - used to track, authorize and un-authorize access
- https://jsonviewer.stack.hu/

- Open Weather API
    - https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    - This API gives us the weather in 3 hour intervals

Environment Variables
- Windows "dir Env:"
- Mac: "env"
- convenience: possibility to modify certain variables without having to touch the code
- security: make sure API keys are not stolen etc.
- create key in terminal by typing:
    - Mac: export + OWM_API_KEY=<key_goes_here>
    - Windows: setx OWM_API_KEY "put_key_here"

"""
import os
import requests
from twilio.rest import Client

"""
Detect if it will rain in the next 12 hours - check weather and send SMS alert
- Check the first four timestamps proved by Api (3 hours apart)
- https://openweathermap.org/weather-conditions 
"""

api_key = os.environ.get('OWM_API_KEY')
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 60.192059,
    "lon": 24.945831,
    "cnt": 4, #only chck the first four timestamps = 12 hours
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

#for SMS - Twilio
account_sid = os.environ.get('ACC_SID')
auth_token = os.environ.get("AUTH_TOKEN")
my_twilio_nr = os.environ.get("MY_TWILIO_NR")
my_phone_number = os.environ.get("MY_NR")

#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain == False:
    #set up Twilio client
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Remember to bring your umbrella!",
        from_=my_twilio_nr,
        to=my_phone_number,
    )

    print(message.status)



