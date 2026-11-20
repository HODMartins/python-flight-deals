import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self._account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self._auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        
    def send_message(self, price, origin_airport, destination_airport, from_date, to_date= None):
        client = Client(self._account_sid, self._auth_token)
        message = client.messages.create(
            body = (
                f"LOW PRICE ALERT!\n"
                f"From {origin_airport} to {destination_airport}\n"
                f"For only CAD {price} on {from_date}"
                ),
            from_='+12623469103',
            to='+12269612726',
            )
        print(message.status)