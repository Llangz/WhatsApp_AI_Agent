from .base_agent import BaseAgent
from crewai import Task, Crew
import logging

class MarketingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Marketing Specialist",
            role="Marketing Campaign Manager",
            goal="Create and execute effective marketing campaigns that drive customer engagement and sales",
            backstory="""You are an experienced marketing specialist with expertise in creating 
            engaging WhatsApp marketing campaigns. You understand customer psychology and know 
            how to craft messages that drive action while maintaining brand voice and compliance."""
        )

    def create_campaign(self, campaign_details: dict) -> str:
        """
        Create a marketing campaign message based on the provided details
        """
        try:
            task = Task(
                description=f"""
                Create a compelling WhatsApp marketing message for the following campaign:
                Product: {campaign_details.get('product')}
                Target Audience: {campaign_details.get('target_audience')}
                Key Message: {campaign_details.get('key_message')}
                Call to Action: {campaign_details.get('call_to_action')}
                
                The message should be:
                - Engaging and personal
                - Clear and concise
                - Include a strong call to action
                - Follow WhatsApp marketing best practices
                """,
                agent=self.agent,
                expected_output="A well-crafted WhatsApp marketing message that is engaging, clear, and includes a strong call to action."
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
            logging.error(f"Error creating campaign: {str(e)}")
            # Return a fallback message if AI generation fails
            return f"""🎉 Special Offer: {campaign_details.get('product')}!

{campaign_details.get('key_message')}

{campaign_details.get('call_to_action')}

Reply 'YES' to learn more!""" 