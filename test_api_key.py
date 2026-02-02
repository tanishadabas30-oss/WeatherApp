# test_api_key.py
import os
from dotenv import load_dotenv
import requests

print("=" * 60)
print("API KEY VERIFICATION TEST")
print("=" * 60)

print("\n1. Loading .env file...")
load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')

print(f"\n2. API Key Status:")
if api_key:
    print(f"   ✓ API key found in .env file")
    print(f"   Length: {len(api_key)} characters")
    print(f"   First 5 chars: {api_key[:5]}")
    print(f"   Last 5 chars: {api_key[-5:]}")
    
    if len(api_key) != 32:
        print(f"   WARNING: Key should be 32 characters, but is {len(api_key)}")
else:
    print("   X API key NOT found!")
    print("\n   Your .env file should contain:")
    print("   WEATHER_API_KEY=your_actual_key_here")
    print("\n   Press Enter to exit...")
    input()
    exit()

print(f"\n3. Testing API Key with OpenWeatherMap...")
print(f"   Making request to API...")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'London',
    'appid': api_key,
    'units': 'metric'
}

try:
    response = requests.get(url, params=params, timeout=10)
    
    if response.status_code == 200:
        print("\n" + "=" * 60)
        print("SUCCESS - API KEY IS VALID!")
        print("=" * 60)
        data = response.json()
        print(f"\nTest Result:")
        print(f"   City: {data['name']}, {data['sys']['country']}")
        print(f"   Temperature: {data['main']['temp']}C")
        print(f"   Weather: {data['weather'][0]['description']}")
        print("\nYour weather app should work now!")
        
    elif response.status_code == 401:
        print("\n" + "=" * 60)
        print("ERROR - API KEY IS INVALID!")
        print("=" * 60)
        print("\nPossible reasons:")
        print("   1. Key is incorrect")
        print("   2. Key not activated yet (wait 10-60 minutes)")
        print("   3. Extra spaces/characters in .env file")
        print("\nYour .env file should look like this:")
        print("   WEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6")
        
    else:
        print(f"\nUnexpected response: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
except Exception as e:
    print(f"\nError: {e}")

print("\n" + "=" * 60)
print("Press Enter to exit...")
input()