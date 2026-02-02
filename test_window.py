# test_api_key.py
import os
from dotenv import load_dotenv
import requests

print("=" * 60)
print("API KEY VERIFICATION TEST")
print("=" * 60)

# Load .env file
print("\n1. Loading .env file...")
load_dotenv()

# Get API key
api_key = os.getenv('WEATHER_API_KEY')

print(f"\n2. API Key Status:")
if api_key:
    print(f"   ✓ API key found in .env file")
    print(f"   Length: {len(api_key)} characters")
    print(f"   First 5 chars: {api_key[:5]}")
    print(f"   Last 5 chars: {api_key[-5:]}")
    
    if len(api_key) != 32:
        print(f"   ⚠ WARNING: Key should be 32 characters, but is {len(api_key)}")
else:
    print("   ✗ API key NOT found!")
    print("   Make sure your .env file has:")
    print("   WEATHER_API_KEY=your_actual_key_here")
    input("\nPress Enter to exit...")
    exit()

# Test API key with actual request
print(f"\n3. Testing API Key with OpenWeatherMap:")
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
        print("✓✓✓ API KEY IS VALID! ✓✓✓")
        print("=" * 60)
        data = response.json()
        print(f"\nTest Result:")
        print(f"   City: {data['name']}, {data['sys']['country']}")
        print(f"   Temperature: {data['main']['temp']}°C")
        print(f"   Weather: {data['weather'][0]['description']}")
        print("\n✓ Your weather app should work now!")
        
    elif response.status_code == 401:
        print("\n" + "=" * 60)
        print("✗✗✗ API KEY IS INVALID! ✗✗✗")
        print("=" * 60)
        print("\nPossible reasons:")
        print("   1. Key is incorrect (copy it again carefully)")
        print("   2. Key is not activated yet (wait 10-60 minutes)")
        print("   3. Extra spaces/characters in .env file")
        print("\nYour .env file should look like this:")
        print("   WEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6")
        print("   (no spaces, no quotes)")
        
    else:
        print(f"\n⚠ Unexpected response code: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
except requests.exceptions.ConnectionError:
    print("\n✗ No internet connection!")
    print("   Check your network and try again.")
    
except requests.exceptions.Timeout:
    print("\n✗ Request timed out!")
    print("   OpenWeatherMap server is slow. Try again.")
    
except Exception as e:
    print(f"\n✗ Error: {e}")

print("\n" + "=" * 60)
input("\nPress Enter to exit...")