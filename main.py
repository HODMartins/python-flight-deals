#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pydoc import describe

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import FlightData
from notification_manager import NotificationManager


today = datetime.now()
tomorrow = today + timedelta(days=1)
six_months_from_today = today + timedelta(days=6 * 30)  # Approximation of 6 months




data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification = NotificationManager()


sheet_data = data_manager.get_sheety_data()

pprint(sheet_data)

# Select departure and destination
departure = sheet_data[1]   # Toronto
# destination = sheet_data[3] # Manchester

# Get destination details
dest_iata_code = sheet_data[0]["iataCode"]
dest_row_id = sheet_data[0]["id"]
current_price = sheet_data[0]["lowestPrice"]

print(dest_iata_code)
print(dest_row_id)
print(current_price)

# Search for flights
flight = flight_search.check_flights(
    departure_city_code=departure["iataCode"],
    arrival_city_code=dest_iata_code,
    from_time=tomorrow,
    to_time=six_months_from_today,
)

# Combine all flights
best_flights = flight.get("best_flights", [])
other_flights = flight.get("other_flights", [])

all_flights = best_flights + other_flights

# Find cheapest flight
cheapest_flight = flight_data.find_cheapest_flight(all_flights)



if cheapest_flight.price != "N/A":
    # Update only if the new price is lower
    if current_price is None or cheapest_flight.price < current_price:

        data_manager.update_current_price(
            row_id=dest_row_id,
            new_price=cheapest_flight.price
        )
        notification.send_message(
            price=cheapest_flight.price, 
            origin_airport=cheapest_flight.origin_airport,
            destination_airport=cheapest_flight.destination_airport,
            from_date=cheapest_flight.from_date
            )
        print(f"Updated flight price to {dest_iata_code} with ${cheapest_flight.price}")
        
# if cheapest_flight is not None:

#     print(f"Destination: {dest_iata_code}")
#     print(f"Row ID: {dest_row_id}")
#     print(f"Cheapest Price: {cheapest_flight.price}")
#     print(f"Current Price: {current_price}")


# from twilio.rest import Client
# from dotenv import load_dotenv

# load_dotenv()

