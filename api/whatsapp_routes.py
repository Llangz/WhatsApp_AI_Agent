from fastapi import APIRouter, HTTPException, Request
from services.whatsapp_service import WhatsAppService
from agents.marketing_agent import MarketingAgent
from agents.customer_service_agent import CustomerServiceAgent
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
whatsapp_service = WhatsAppService()
marketing_agent = MarketingAgent()
customer_service_agent = CustomerServiceAgent()

class CampaignRequest(BaseModel):
    numbers: List[str]
    product: str
    target_audience: str
    key_message: str
    call_to_action: str

class MessageRequest(BaseModel):
    to_number: str
    message: str

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    """
    Handle incoming WhatsApp messages
    """
    try:
        data = await request.json()
        message_body = data.get('Body', '')
        from_number = data.get('From', '').replace('whatsapp:', '')
        
        # Process the message using the customer service agent
        response = customer_service_agent.handle_inquiry(message_body)
        
        # Send the response back to the customer
        await whatsapp_service.send_message(from_number, response)
        
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/campaign")
async def create_campaign(campaign: CampaignRequest):
    """
    Create and send a marketing campaign
    """
    try:
        # Generate campaign message using the marketing agent
        campaign_details = {
            "product": campaign.product,
            "target_audience": campaign.target_audience,
            "key_message": campaign.key_message,
            "call_to_action": campaign.call_to_action
        }
        
        message = marketing_agent.create_campaign(campaign_details)
        
        # Send the campaign to all numbers
        results = await whatsapp_service.send_campaign(campaign.numbers, message)
        
        return {
            "status": "success",
            "message": "Campaign sent successfully",
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/message")
async def send_message(message_request: MessageRequest):
    """
    Send a single WhatsApp message
    """
    try:
        result = await whatsapp_service.send_message(message_request.to_number, message_request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 