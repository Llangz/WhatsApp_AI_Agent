import requests
import json
import re

def validate_phone_numbers(numbers):
    """Validate phone number format"""
    validated_numbers = []
    for number in numbers:
        # Remove any spaces or special characters
        number = re.sub(r'[^0-9+]', '', number)
        
        # Check if number starts with + and has at least 10 digits
        if not number.startswith('+'):
            print(f"Invalid number {number}: Must start with country code (e.g., +1)")
            continue
        
        if len(number) < 10:
            print(f"Invalid number {number}: Too short")
            continue
            
        validated_numbers.append(number)
    
    return validated_numbers

def send_test_campaign():
    url = "http://127.0.0.1:8000/whatsapp/campaign"
    
    # Get phone numbers
    print("\nEnter phone numbers (one per line, press Enter twice to finish):")
    numbers = []
    while True:
        number = input("Enter number (or press Enter to finish): ")
        if not number:
            break
        numbers.append(number)
    
    # Validate numbers
    validated_numbers = validate_phone_numbers(numbers)
    if not validated_numbers:
        print("No valid numbers provided. Exiting.")
        return
    
    # Campaign details
    campaign_data = {
        "numbers": validated_numbers,
        "product": "Premium Subscription",
        "target_audience": "Business Professionals",
        "key_message": "Boost your productivity with our AI-powered features",
        "call_to_action": "Reply 'PREMIUM' to get started with a 7-day free trial!"
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("\nSending campaign...")
        # Send POST request
        response = requests.post(url, json=campaign_data, headers=headers)
        
        # Print response
        print("\nStatus Code:", response.status_code)
        
        try:
            response_data = response.json()
            print("Response:", response_data)
            
            if response_data.get('status') == 'error':
                print("\nError Details:")
                print(response_data.get('message', 'Unknown error'))
            else:
                print("\nCampaign Results:")
                for result in response_data.get('results', []):
                    print(f"\nNumber: {result['number']}")
                    print(f"Status: {result['result']['status']}")
                    if result['result'].get('message_id'):
                        print(f"Message ID: {result['result']['message_id']}")
                    
        except json.JSONDecodeError:
            print("Response (raw):", response.text)
        
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server. Make sure the server is running at http://127.0.0.1:8000")
    except Exception as e:
        print("\nError:", str(e))

if __name__ == "__main__":
    print("WhatsApp Campaign Test Script")
    print("============================")
    send_test_campaign() 