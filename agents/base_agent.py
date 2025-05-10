from crewai import Agent
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, name: str, role: str, goal: str, backstory: str):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.agent = self._create_agent()

    def _create_agent(self) -> Agent:
        return Agent(
            name=self.name,
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            allow_delegation=True,
            llm_model="gpt-3.5-turbo"  # Using a more cost-effective model
        )

    def get_agent(self) -> Agent:
        return self.agent 