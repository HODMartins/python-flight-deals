import os
import requests
from dotenv import load_dotenv

load_dotenv()

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("AUTHORIZATION", "Authorization not found")
}
SHEETY_URL = "https://api.sheety.co/ec0469c2513ef14c6afecb223310e2bf/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._url = SHEETY_URL
        self._sheety_headers = sheety_headers


    def get_sheety_data(self):
        response = requests.get(
            url=self._url,
            headers=self._sheety_headers
        )
        response.raise_for_status()

        return [
            {"id": item["id"], "iataCode": item["iataCode"], "lowestPrice": item.get("lowestPrice")}
            for item in response.json()["prices"]
        ]


    def update_current_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(
            url=f"{self._url}/{row_id}",
            json=new_data,
            headers=self._sheety_headers
        )
        response.raise_for_status()
        


    