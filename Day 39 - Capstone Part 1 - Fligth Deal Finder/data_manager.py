from pprint import pprint
import requests
import os
from requests.auth import HTTPBasicAuth

FLIGHT_SHEET_ENDPOINT = os.environ.get('FLIGHT_SHEET_GET_API')

class DataManager:

    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        """Fetches data from Google spreadsheets"""
        response  = requests.get(FLIGHT_SHEET_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            self.destination_data = data["prices"]
            return self.destination_data
        else:
            print(f"Error getting prices from Google file, status code {response.status_code}")

    def update_destination_codes(self):
        """Updates the IATA code in the spreadsheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response =requests.put(
                url=f"{FLIGHT_SHEET_ENDPOINT}/{city['id']}",json=new_data)
            print(response.text)