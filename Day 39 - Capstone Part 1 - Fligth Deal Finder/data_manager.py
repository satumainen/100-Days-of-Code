from pprint import pprint
import requests
import os

FLIGHT_SHEET_GET_API = os.environ.get("FLIGHT_SHEET_GET_API")
FLIGHT_SHEET_POST_API = os.environ.get("FLIGHT_SHEET_POST_API")
FLIGHT_SHEET_PUT_API = os.environ.get("FLIGHT_SHEET_PUT_API")

class DataManager:

    def __init__(self):
        self.prices_data = []

    def get_prices(self):
        """Fetches data from Google spreadsheets"""
        response  = requests.get(FLIGHT_SHEET_GET_API)
        if response.status_code == 200:
            data = response.json()
            prices_data = data["prices"]
            return prices_data
        else:
            print(f"Error getting prices, status code {response.status_code}")

    def update_iata_code(self, city, iata_code):
        update_params = {
            "City": city,
            "IATA CODE": iata_code,
        }
        endpoint = f"{FLIGHT_SHEET_PUT_API}{city}"



