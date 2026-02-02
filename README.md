# Weather App 🌤️

Hey there! This is a simple desktop weather app I built using Python and Tkinter. It grabs real-time weather data from OpenWeatherMap and displays it in a clean GUI. Nothing fancy, but it gets the job done!

## What It Does

Pretty straightforward - you type in a city name, hit enter (or click the button), and boom - you get the current weather. Temperature, humidity, wind speed, all that good stuff.

I built this because I was tired of opening my browser just to check the weather. Plus, it was a fun way to practice working with APIs and building desktop GUIs.

## Screenshots

When you first open it, it looks like this:
- A text box where you type the city name
- A big green "Get Weather" button
- That's it. Simple.

After you search for a city:
- Shows the temperature (big and bold so you can't miss it)
- Weather description with a cute emoji
- All the extra details like humidity and wind speed

_(I should probably add actual screenshots here at some point...)_

## What You Need

- Python 3.8 or newer (I used 3.13 but anything recent should work)
- An OpenWeatherMap API key (it's free, takes like 2 minutes to get)
- That's basically it

## Getting Started

### 1. Grab the Code

Download this project or clone it:
```bash
git clone https://github.com/tanishadabas30-oss/weather-app.git
cd weather-app
```

### 2. Set Up a Virtual Environment

I always use virtual environments for Python projects. Keeps things clean.
```bash
python -m venv venv
```

Then activate it:
- **Windows:** `.\venv\Scripts\Activate`
- **Mac/Linux:** `source venv/bin/activate`

You'll know it worked when you see `(venv)` at the start of your terminal line.

### 3. Install the Dependencies

Only two packages needed:
```bash
pip install requests python-dotenv
```

Or if you have the requirements file:
```bash
pip install -r requirements.txt
```

### 4. Get Your API Key

Head over to [OpenWeatherMap](https://openweathermap.org/api) and sign up. It's free and they don't even ask for a credit card.

Once you're signed in:
1. Go to your API keys page
2. Copy that long string of letters and numbers
3. Keep it handy for the next step

**Important:** New API keys can take like 30-60 minutes to activate. So if it doesn't work right away, just wait a bit and try again.

### 5. Add Your API Key

Create a file called `.env` in the main project folder (same place as `main.py`).

Put this in it:
```
WEATHER_API_KEY=30f6e7b1488a03b8e6d81a7aa8f4836c
```

Just that one line. No quotes, no spaces around the equals sign. Should look something like:

**Don't commit this file to GitHub!** The `.gitignore` should already be set up to ignore it, but just FYI.

## Running It

Make sure your virtual environment is active (you should see `(venv)` in your terminal), then:
```bash
python main.py
```

That's it! The window should pop up and you're good to go.

## Project Structure

Here's how everything is organized:
```
weather-app/
├── config/
│   ├── config.py          # All the settings and API stuff
│   └── __init__.py
├── src/
│   ├── gui.py             # The Tkinter interface
│   ├── weather_api.py     # Handles talking to OpenWeatherMap
│   ├── utils.py           # Random helper functions
│   └── __init__.py
├── venv/                  # Virtual environment (don't touch this)
├── .env                   # Your API key goes here
├── .gitignore
├── main.py                # Run this file
├── requirements.txt
└── README.md              # You are here
```

Nothing too crazy. I tried to keep it organized so it's easy to find stuff.

## How It Works (Quick Version)

1. You type a city name
2. The app validates it (makes sure you didn't type "123" or something dumb)
3. It sends a request to OpenWeatherMap with your API key
4. OpenWeatherMap sends back a bunch of JSON data
5. The app pulls out the useful bits (temperature, weather description, etc.)
6. Formats it nicely and shows it in the window

The actual API call is pretty simple - just a GET request with the city name and API key as parameters.

## Common Issues

**"Invalid API Key"**
- Wait 30-60 minutes if you just signed up
- Double-check your `.env` file - no spaces, no quotes
- Make sure you copied the whole key

**"City not found"**
- Check your spelling
- Try bigger cities first (London, New York, etc.)
- Some tiny towns might not be in the database

**Window doesn't show up**
- Press Alt+Tab - it might be hiding behind other windows
- On Linux, you might need to install tkinter: `sudo apt-get install python3-tk`

**Import errors**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

## Things I Might Add Later

Just some ideas I've been thinking about:
- [ ] 5-day forecast instead of just current weather
- [ ] Ability to switch between Celsius and Fahrenheit
- [ ] Remember recent searches
- [ ] Weather icons (right now it's just emojis)
- [ ] Dark mode because why not
- [ ] Maybe save favorite cities

Feel free to add any of these yourself if you want! Pull requests welcome.

## Tech Stack

- **Python** - Obviously
- **Tkinter** - For the GUI (comes with Python, no extra install needed)
- **Requests** - To make the API calls
- **python-dotenv** - To load environment variables
- **OpenWeatherMap API** - Where the weather data comes from

## Contributing

If you want to improve this or add features, go for it! Just:
1. Fork the repo
2. Make your changes
3. Test it to make sure it works
4. Send a pull request

No formal process or anything. Just keep the code readable and maybe add a comment or two.

## Credits

- OpenWeatherMap for the free API
- Stack Overflow for helping me debug that one weird import error
- My friend who kept asking "is it done yet?" which motivated me to actually finish it

## Contact

If you run into issues or have questions:
- Open an issue on GitHub
- Or email me at tanishadabas30@gmail.com

I'll try to help if I can, but no promises I'll respond super quickly!

---

**Made by [Tanisha]** 

Built this over a couple weekends while learning API integration. Hope you find it useful! ☕
