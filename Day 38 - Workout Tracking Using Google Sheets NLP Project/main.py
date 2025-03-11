"""
This project allows the user to add information on their training and get statistics and calories burnt in
Google Sheets, by using an NLP exercise API to process text input. Sheety is used to upload information to
a Google sheet.

This project combines previously learnt things:
- Python DateTime strftime
- APIs and making POST requests
- creating authorization headers
- creating environmental variables
"""

import os
import datetime
import requests

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
#Bearer authentication
AUTHENTICATION_TOKEN  = os.environ.get('AUTHENTICATION_TOKEN')
SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')


exercise_text = input("Enter exercise information: ")
today = datetime.datetime.today().strftime("%d/%m/%Y")
time_now = datetime.datetime.now().strftime("%H:%M:%S")
print(today)
print(time_now)

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutTracking/workouts"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

params = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 175,
    "age": 30
}

response = requests.post(nutritionix_endpoint, json=params, headers=headers)
result = response.json()
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }

bearer_headers = {
"Authorization": f"Bearer {AUTHENTICATION_TOKEN}",
}

sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)

