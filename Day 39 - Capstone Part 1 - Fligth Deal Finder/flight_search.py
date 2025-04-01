import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    ##documentation: https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
    #domunetation: https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
    #documentation: https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference
    #https://developers.amadeus.com/


    AMADEUS_FLIGHT_SEARCH_API = ""

    def __init__(self):
        self.flights = []

    def get_iata_code(self, city):
        print("In Flight Search")
        code = "test"
        return code