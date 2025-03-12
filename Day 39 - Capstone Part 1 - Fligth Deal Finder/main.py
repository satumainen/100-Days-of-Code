#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

def main():
    dm = DataManager()
    prices = dm.get_prices()
    pprint.pprint(prices)
    for city in prices:
        if city["iataCode"] == "":
            print("No iata code")
            flight_search = FlightSearch()
            iata_code = flight_search.get_iata_code(city)
            print("IATA CODE: ", iata_code)
            #update iataCode with data_manager

main()