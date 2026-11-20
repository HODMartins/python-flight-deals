import os
import sqlite3
import serpapi
from dotenv import load_dotenv
import requests_cache


load_dotenv()
URL = "https://serpapi.com/search?engine=google_flights"
#This class is responsible for talking to the Flight Search API.

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("SERPAPI_KEY", "SerpApi key not found")

    def check_flights(self, departure_city_code, arrival_city_code, from_time, to_time = None, currency="CAD", type=2, hl="en"):
        parameter = {
            "engine": "google_flights",
            "departure_id": f"{departure_city_code}",
            "arrival_id": f"{arrival_city_code}",
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "api_key": self._api_key
        }
        try:    
            session = requests_cache.CachedSession("flight_search_cache", backend="sqlite",  expire_after=3600)
            results = session.get(url = URL, params=parameter)
            results.raise_for_status()
            return results.json()
        except (requests_cache.exceptions.RequestException, ValueError) as error:
            print(f"Flight search failed: {error}")
            return {}