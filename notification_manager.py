from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = ""
        self.auth_token = ""

    def send_sms(self, body):
        self.client = Client(self.account_sid, self.auth_token)

        message = self.client.messages \
            .create(
            body=body,
            from_='',
            to=''
        )

        print(message.status)
