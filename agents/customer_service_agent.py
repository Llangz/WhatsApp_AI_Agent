from .base_agent import BaseAgent
from crewai import Task, Crew
import logging

class CustomerServiceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Customer Service Representative",
            role="Customer Support Specialist",
            goal="Provide excellent customer service and resolve customer inquiries effectively",
            backstory="""You are a knowledgeable and empathetic customer service representative 
            with extensive experience in handling customer inquiries via WhatsApp. You excel at 
            understanding customer needs and providing timely, accurate solutions while maintaining 
            a friendly and professional tone."""
        )

    def handle_inquiry(self, customer_message: str, context: dict = None) -> str:
        """
        Handle a customer inquiry and generate an appropriate response
        """
        try:
            task = Task(
                description=f"""
                Respond to the following customer inquiry:
                Customer Message: {customer_message}
                
                Additional Context:
                {context if context else 'No additional context provided'}
                
                Guidelines:
                - Be professional and empathetic
                - Provide clear and accurate information
                - If the inquiry is about a product, include relevant details
                - If the inquiry requires escalation, indicate this clearly
                - Keep the response concise but complete
                """,
                agent=self.agent,
                expected_output="A professional, empathetic, and helpful response that addresses the customer's inquiry effectively."
            )
            
            # Create a crew with the task
            crew = Crew(
                agents=[self.agent],
                tasks=[task],
                verbose=True
            )
            
            # Execute the crew and get the result
            result = crew.kickoff()
            return result
            
        except Exception as e:
            logging.error(f"Error handling inquiry: {str(e)}")
            return "Thank you for your message. Our team will get back to you shortly. For immediate assistance, please call our support line."

    def handle_complaint(self, complaint: str, customer_history: dict = None) -> str:
        """
        Handle a customer complaint and generate an appropriate response
        """
        try:
            task = Task(
                description=f"""
                Address the following customer complaint:
                Complaint: {complaint}
                
                Customer History:
                {customer_history if customer_history else 'No previous history available'}
                
                Guidelines:
                - Show empathy and understanding
                - Acknowledge the issue
                - Provide a clear solution or next steps
                - Offer appropriate compensation if necessary
                - Maintain a professional and calm tone
                """,
                agent=self.agent,
                expected_output="A professional and empathetic response that acknowledges the complaint and provides a clear solution or next steps."
            )
            
            # Create a crew with the task
            crew = Crew(
                agents=[self.agent],
                tasks=[task],
                verbose=True
            )
            
            # Execute the crew and get the result
            result = crew.kickoff()
            return result
            
        except Exception as e:
            logging.error(f"Error handling complaint: {str(e)}")
            return "We apologize for any inconvenience. Our team has been notified of your concern and will address it promptly. Please expect a follow-up within 24 hours." 