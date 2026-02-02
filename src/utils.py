# src/utils.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import Config
def validate_city_name(city_name):
    if city_name is None:
        return False, "Please enter a city name"
    
    city_name = city_name.strip()
    
    if not city_name:
        return False, "Please enter a city name"
    
    if len(city_name) < 2:
        return False, "City name is too short"
    
    if len(city_name) > 50:
        return False, "City name is too long"
    
    for character in city_name:
        if character.isdigit():
            return False, "City name cannot contain numbers"
    
    for character in city_name:
        if character.isalpha() or character in [' ', '-', "'"]:
            continue
        return False, "City name contains invalid characters"
    
    return True, "Valid"

def format_temperature(temp, unit=None):
    if unit is None:
        unit = Config.DEFAULT_UNITS
    rounded_temp = round(temp, 1)
    if unit == "metric":
        return f"{rounded_temp}°C"
    elif unit == "imperial":
        return f"{rounded_temp}°F"
    else:
        return f"{rounded_temp}K"

def capitalize_description(description):
    if not description:
        return "No Description"
    words = description.split()
    return ' '.join([word.capitalize() for word in words])

def format_wind_speed(speed, unit=None):
    if unit is None:
        unit = Config.DEFAULT_UNITS
    rounded_speed = round(speed, 1)
    if unit == "metric":
        return f"{rounded_speed} m/s"
    elif unit == "imperial":
        return f"{rounded_speed} mph"
    else:
        return f"{rounded_speed}"

def format_humidity(humidity):
    return f"{round(humidity)}%"

def format_pressure(pressure):
    return f"{round(pressure)} hPa"

def format_city_display(city, country):
    return f"{city}, {country}"

def get_weather_emoji(icon_code):
    if not icon_code or len(icon_code) < 2:
        return '🌡️'
    code = icon_code[0:2]
    emojis = {
        '01': '☀️', '02': '⛅', '03': '☁️', '04': '☁️',
        '09': '🌧️', '10': '🌦️', '11': '⛈️', '13': '❄️', '50': '🌫️'
    }
    return emojis.get(code, '🌡️')