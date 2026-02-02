# src/weather_api.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
from config.config import Config

def fetch_weather_data(city_name):
    """
    Fetches weather data for a given city from OpenWeatherMap API.
    """
    
    # Build the complete URL
    url = f"{Config.BASE_URL}{Config.WEATHER_ENDPOINT}"
    
    # Query parameters
    params = {
        'q': city_name,
        'appid': Config.API_KEY,
        'units': Config.DEFAULT_UNITS,
        'lang': Config.DEFAULT_LANGUAGE
    }
    
    try:
        # Make HTTP GET request
        response = requests.get(url, params=params, timeout=Config.TIMEOUT)
        
        # Check response status
        if response.status_code == 200:
            json_data = response.json()
            return {
                'success': True,
                'data': json_data
            }
        
        elif response.status_code == 404:
            return {
                'success': False,
                'error': Config.ERROR_MESSAGES['city_not_found']
            }
        
        elif response.status_code == 401:
            return {
                'success': False,
                'error': Config.ERROR_MESSAGES['invalid_api_key']
            }
        
        else:
            return {
                'success': False,
                'error': f"API Error: {response.status_code}"
            }
    
    except Timeout:
        return {
            'success': False,
            'error': Config.ERROR_MESSAGES['timeout']
        }
    
    except ConnectionError:
        return {
            'success': False,
            'error': Config.ERROR_MESSAGES['network_error']
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': f"Unexpected error: {str(e)}"
        }


def parse_weather_data(raw_data):
    """
    Extracts and formats relevant weather information from raw API response.
    """
    
    try:
        temperature = raw_data['main']['temp']
        feels_like = raw_data['main']['feels_like']
        humidity = raw_data['main']['humidity']
        pressure = raw_data['main']['pressure']
        wind_speed = raw_data['wind']['speed']
        description = raw_data['weather'][0]['description'].title()
        icon = raw_data['weather'][0]['icon']
        city = raw_data['name']
        country = raw_data['sys']['country']
        
        cleaned_data = {
            'city': city,
            'country': country,
            'temperature': round(temperature, 1),
            'feels_like': round(feels_like, 1),
            'description': description,
            'humidity': humidity,
            'wind_speed': round(wind_speed, 1),
            'pressure': pressure,
            'icon': icon
        }
        
        return cleaned_data
    
    except KeyError as e:
        print(f"Error parsing weather data: Missing key {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected error parsing weather data: {e}")
        return None


def get_weather(city_name):
    """
    Main function that combines fetching and parsing.
    """
    
    # Fetch raw data
    result = fetch_weather_data(city_name)
    
    # Check if fetch was successful
    if not result['success']:
        return result
    
    # Parse the raw data
    parsed_data = parse_weather_data(result['data'])
    
    # Check if parsing was successful
    if parsed_data is None:
        return {
            'success': False,
            'error': 'Failed to parse weather data'
        }
    
    # Return success with parsed data
    return {
        'success': True,
        'data': parsed_data
    }