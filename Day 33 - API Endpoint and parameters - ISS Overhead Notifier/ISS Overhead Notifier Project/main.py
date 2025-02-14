"""
- API: Application Programming Interface
    - set of commands, functions, protocols and objects
    - programmers use them to create software or interact with an external system
- barrier between your program and an external system
    - structure your request appropriately
    - get a response
- API Requests

International Space Station Current Location API
- End point: returns the location in JSON format
    - describes iss_position in terms of longitude and latitude
    - every time link is refreshed, the new current location is returned
    - http://api.open-notify.org/iss-now.json
- JSON Viewer Awesome Chrome plugin
    - shows JSON data in a nice tree structure in the browser
- JSON is very compact, and can be transported effectively over the internet

Response Codes
- 1XX: Hold on
- 2XX: Successful
- 3XX: Permission Denied
- 4XX: "You screwed up", user mistake BAD REQUEST
- 5XX; "I screwed up", service provider mistake

Raising Exceptions
- generate exceptions with the request module
- response.raise_for_status()

Parameters
- The ISS API is easy and does not have parameters, but some API's allow them
- Sunrise and Sunset API https://sunrise-sunset.org/api
    - needs a location to be provided, latitude and longitude
    - specified parameters and formats

Sample Request
- Endpoint url ? param. name = value & ...

"""


import requests # must be installed, not pre-built in Python
from datetime import datetime
import smtplib
import time

MY_EMAIL = '<EMAIL>' #placeholder
MY_PASSWORD = '<PASSWORD>' #placeholder
MY_LAT =  60.454510
MY_LONG = 22.264824

response = requests.get(url="http://api.open-notify.org/iss-now.json") #url = endpoint
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
#Parameters needed for the sunrise API, formatted as the required dictionary

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, #set 24 h clock instead of 12h
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)  # parameters dictionary input
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[
                      0])  # isolate hour by splitting, first by T and then by : into a list
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour  # compare with time now

    if time_now >= sunset or time_now <= sunrise:
        return True


def is_iss_overhead():
    if 55 <= iss_latitude <= 65 and 17 <= iss_longitude <= 27:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
        )


