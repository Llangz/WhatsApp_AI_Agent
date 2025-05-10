import requests
import json
import time

def test_customer_service():
    url = "http://127.0.0.1:8000/whatsapp/webhook"
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "Product Inquiry",
            "message": "Hi, I'm interested in your Premium Subscription. What features does it include?",
            "context": {"product": "Premium Subscription", "features": ["AI-powered responses", "24/7 support", "Analytics dashboard"]}
        },
        {
            "name": "Technical Support",
            "message": "I'm having trouble sending messages through the platform. Can you help?",
            "context": {"issue_type": "technical", "platform": "WhatsApp"}
        },
        {
            "name": "Pricing Question",
            "message": "How much does the Premium plan cost?",
            "context": {"product": "Premium Subscription", "pricing": {"monthly": "$29.99", "yearly": "$299.99"}}
        }
    ]
    
    print("WhatsApp Customer Service Chatbot Test")
    print("=====================================")
    
    for scenario in test_scenarios:
        print(f"\nTesting Scenario: {scenario['name']}")
        print(f"Customer Message: {scenario['message']}")
        
        # Prepare the webhook payload
        payload = {
            "Body": scenario['message'],
            "From": "whatsapp:+1234567890",  # Test number
            "context": scenario['context']
        }
        
        try:
            # Send the request
            response = requests.post(url, json=payload)
            
            # Print response
            print("\nStatus Code:", response.status_code)
            
            try:
                response_data = response.json()
                print("Response:", response_data)
            except json.JSONDecodeError:
                print("Response (raw):", response.text)
                
        except requests.exceptions.ConnectionError:
            print("\nError: Could not connect to the server. Make sure the server is running at http://127.0.0.1:8000")
        except Exception as e:
            print("\nError:", str(e))
        
        # Wait a bit between scenarios
        time.sleep(2)

if __name__ == "__main__":
    test_customer_service() 