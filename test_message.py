import requests
import json
import re

def validate_phone_number(phone_number):
    """Validate phone number format"""
    # Remove any spaces or special characters
    phone_number = re.sub(r'[^0-9+]', '', phone_number)
    
    # Check if number starts with + and has at least 10 digits
    if not phone_number.startswith('+'):
        return False, "Phone number must start with country code (e.g., +1)"
    
    if len(phone_number) < 10:
        return False, "Phone number is too short"
        
    return True, phone_number

def send_test_message():
    url = "http://127.0.0.1:8000/whatsapp/message"
    
    # Get and validate phone number
    while True:
        phone_number = input("Enter the recipient's WhatsApp number (with country code, e.g., +1234567890): ")
        is_valid, result = validate_phone_number(phone_number)
        
        if is_valid:
            phone_number = result
            break
        else:
            print(f"Invalid phone number: {result}")
            print("Please try again.")
    
    # Message data
    data = {
        "to_number": phone_number,
        "message": "Hello! This is a test message from LipaChat API"
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("\nSending message...")
        # Send POST request
        response = requests.post(url, json=data, headers=headers)
        
        # Print response
        print("\nStatus Code:", response.status_code)
        
        try:
            response_data = response.json()
            print("Response:", response_data)
            
            if response_data.get('status') == 'error':
                print("\nError Details:")
                print(response_data.get('message', 'Unknown error'))
        except json.JSONDecodeError:
            print("Response (raw):", response.text)
        
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server. Make sure the server is running at http://127.0.0.1:8000")
    except Exception as e:
        print("\nError:", str(e))

if __name__ == "__main__":
    print("WhatsApp Message Test Script")
    print("===========================")
    send_test_message()