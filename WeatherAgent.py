# WeatherAgent.py

from BaseAgent import BaseAgent
import random

def weather_action(location: str):
    return f"The current weather in {location} is Sunny with {random.randint(20,45)} degree fareheit temperature."

class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="WeatherAgent",
            description="Provides mock weather data for a given location.",
            action=weather_action
        )

