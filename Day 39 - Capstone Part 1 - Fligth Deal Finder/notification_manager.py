import os
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.

MY_TWILIO_NR = os.environ['MY_TWILIO_NR']
MY_NR = os.environ['MY_NR']
TWILIO_SID = os.environ.get("ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=MY_TWILIO_NR,
            body=message_body,
            to=MY_NR
        )
        # Prints if successfully sent.
        print(message.sid)
