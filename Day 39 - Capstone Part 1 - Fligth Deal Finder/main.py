#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from notification_manager import NotificationManager
import time
from datetime import datetime, timedelta

#starting city
ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    print("In loop in main")
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])

    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )

        # SMS not working? Try whatsapp instead.
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )