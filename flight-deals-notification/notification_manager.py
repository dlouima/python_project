from twilio.rest import Client

TWILIO_SID = "your_twilio_key"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_VIRTUAL_NUMBER = "your twilio phone number"
TWILIO_VERIFIED_NUMBER = "Your phone number"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
