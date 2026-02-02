# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv('WEATHER_API_KEY', '')
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    TIMEOUT = 10
    DEFAULT_UNITS = "metric"
    DEFAULT_LANGUAGE = "en"
    WEATHER_ENDPOINT = "/weather"
    FORECAST_ENDPOINT = "/forecast"
    
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 600
    BG_COLOR = "#E3F2FD"
    BUTTON_COLOR = "#4CAF50"
    TEXT_COLOR = "#212121"
    
    ERROR_MESSAGES = {
        "no_city": "Please enter a city name",
        "city_not_found": "City not found. Please check spelling.",
        "network_error": "Cannot connect to weather service. Check your internet.",
        "timeout": "Request took too long. Please try again.",
        "invalid_api_key": "API key is invalid. Please check configuration.",
        "unknown": "An unexpected error occurred. Please try again.",
        "invalid_characters": "City name contains invalid characters."
    }
    
    MAX_CITY_LENGTH = 50
    MIN_CITY_LENGTH = 2