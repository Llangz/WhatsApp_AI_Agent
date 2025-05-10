WhatsApp AI Marketing & Customer Care Platform

This is an AI-powered WhatsApp platform that helps businesses automate their marketing and customer care operations. Built with CrewAI, it enables companies to send automated marketing campaigns and build intelligent chatbots to grow their business through WhatsApp.

## Features

- **AI-Powered Marketing Campaigns**
  - Automated campaign message generation
  - Targeted audience messaging
  - Campaign performance tracking

- **Intelligent Customer Service**
  - AI-driven response generation
  - Context-aware conversations
  - Multi-scenario handling

- **WhatsApp Integration**
  - Seamless message delivery
  - Media message support
  - Real-time communication

## Technical Stack

- Python 3.8+
- FastAPI
- CrewAI
- Twilio API
- OpenAI GPT
- RESTful APIs

## Project Structure

```
WhatsApp_AI_Agent/
├── agents/           # AI agents for different tasks
│   ├── base_agent.py
│   ├── marketing_agent.py
│   └── customer_service_agent.py
├── api/             # API endpoints
│   └── whatsapp_routes.py
├── services/        # WhatsApp integration
│   └── whatsapp_service.py
├── models/          # Data models
├── utils/           # Utility functions
├── main.py          # FastAPI application
├── run.py           # Server runner
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WhatsApp_AI_Agent.git
   cd WhatsApp_AI_Agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your credentials:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=your_whatsapp_number
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the application:
   ```bash
   python run.py
   ```

## Testing

1. Test Basic Messaging:
   ```bash
   python test_message.py
   ```

2. Test Marketing Campaigns:
   ```bash
   python test_campaign.py
   ```

3. Test Customer Service Chatbot:
   ```bash
   python test_chatbot.py
   ```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/WhatsApp_AI_Agent](https://github.com/yourusername/WhatsApp_AI_Agent) 
