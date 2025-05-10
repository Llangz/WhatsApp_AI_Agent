from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppService:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.client = Client(self.account_sid, self.auth_token)
        # Use the Twilio WhatsApp sandbox number
        self.whatsapp_number = "whatsapp:+14155238886"  # This is Twilio's WhatsApp sandbox number

    async def send_message(self, to_number: str, message: str):
        """
        Send a WhatsApp message to a specific number
        """
        try:
            # Remove any 'whatsapp:' prefix if it exists
            to_number = to_number.replace('whatsapp:', '')
            
            message = self.client.messages.create(
                body=message,
                from_=self.whatsapp_number,
                to=f'whatsapp:{to_number}'
            )
            return {"status": "success", "message_id": message.sid}
        except TwilioRestException as e:
            return {"status": "error", "message": str(e)}

    async def send_campaign(self, numbers: list, message: str):
        """
        Send a campaign message to multiple numbers
        """
        results = []
        for number in numbers:
            result = await self.send_message(number, message)
            results.append({"number": number, "result": result})
        return results

    async def send_media_message(self, to_number: str, media_url: str, caption: str = None):
        """
        Send a media message (image, video, document) via WhatsApp
        """
        try:
            # Remove any 'whatsapp:' prefix if it exists
            to_number = to_number.replace('whatsapp:', '')
            
            message = self.client.messages.create(
                body=caption,
                media_url=[media_url],
                from_=self.whatsapp_number,
                to=f'whatsapp:{to_number}'
            )
            return {"status": "success", "message_id": message.sid}
        except TwilioRestException as e:
            return {"status": "error", "message": str(e)} 