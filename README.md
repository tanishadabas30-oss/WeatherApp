# 🌤️ Weather Application

A modern desktop weather application built with Python and Tkinter that provides real-time weather information for cities worldwide using the OpenWeatherMap API.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

---

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

---

## ✨ Features

- 🌍 **Global Coverage**: Get weather data for any city worldwide
- 🌡️ **Real-time Data**: Live temperature, humidity, and atmospheric pressure
- 💨 **Wind Information**: Current wind speed in meters per second
- 🌈 **Weather Descriptions**: Clear descriptions with weather emojis
- 🎨 **Modern UI**: Clean, user-friendly interface with intuitive design
- ⚡ **Fast Performance**: Quick API response and efficient data processing
- ✅ **Input Validation**: Smart validation to prevent errors
- 🔒 **Secure**: API keys stored safely in environment variables
- 📱 **Responsive**: Fixed window size optimized for desktop use

---

## 📸 Screenshots

### Main Interface
```
┌─────────────────────────────────────┐
│  Weather Application            [×] │
├─────────────────────────────────────┤
│                                     │
│         🌤️ Weather App              │
│                                     │
│       Enter city name:              │
│     ┌─────────────────────┐        │
│     │     London          │        │
│     └─────────────────────┘        │
│     ┌───────────────────┐          │
│     │   Get Weather     │          │
│     └───────────────────┘          │
└─────────────────────────────────────┘
```

### Weather Results Display
```
┌─────────────────────────────────────┐
│  ☀️ London, GB                       │
│                                     │
│         15.5°C                      │
│                                     │
│      Partly Cloudy                  │
│  ─────────────────────────────────  │
│  Feels like: 14.2°C                 │
│  💧 Humidity: 72%                    │
│  💨 Wind: 4.5 m/s                    │
│  🌡️ Pressure: 1013 hPa               │
└─────────────────────────────────────┘
```

---

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Tkinter** - GUI framework (built-in with Python)
- **Requests** - HTTP library for API calls
- **python-dotenv** - Environment variable management
- **OpenWeatherMap API** - Weather data provider

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
  - Download from: [python.org](https://www.python.org/downloads/)
  - Make sure to check "Add Python to PATH" during installation
  - Verify: `python --version`

- **pip** (Python package manager)
  - Usually comes with Python
  - Verify: `pip --version`

- **Git** (optional, for cloning)
  - Download from: [git-scm.com](https://git-scm.com/)

- **OpenWeatherMap API Key** (free)
  - Sign up at: [openweathermap.org](https://openweathermap.org/api)

---

## 🚀 Installation

### Option 1: Clone the Repository
```bash
# Clone the repository
git clone https://github.com/yourusername/weather-app.git

# Navigate to project directory
cd weather-app
```

### Option 2: Download ZIP

1. Download the ZIP file from GitHub
2. Extract to your desired location
3. Open terminal/PowerShell in the extracted folder

---

### Step-by-Step Setup

#### 1️⃣ Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

#### 2️⃣ Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

**You should see `(venv)` at the start of your terminal prompt.**

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:
```bash
pip install requests python-dotenv
```

---

## ⚙️ Configuration

### 1. Get Your API Key

1. **Sign up** at [OpenWeatherMap](https://openweathermap.org/api)
2. **Verify your email** (check spam folder)
3. **Sign in** to your account
4. Navigate to **[API Keys](https://home.openweathermap.org/api_keys)**
5. **Copy your API key** (32-character string)

**⏰ Note:** New API keys take 10-60 minutes to activate!

---

### 2. Configure Environment Variables

#### Create `.env` File

**In the project root directory**, create a file named `.env`:

**Windows (PowerShell):**
```powershell
New-Item -ItemType File -Path .env
notepad .env
```

**Mac/Linux:**
```bash
touch .env
nano .env
```

#### Add Your API Key

**Add this single line to the `.env` file:**
```
WEATHER_API_KEY=your_actual_api_key_here
```

**Example:**
```
WEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

**⚠️ IMPORTANT:**
- ✅ No spaces around the `=` sign
- ✅ No quotes around the key
- ✅ No semicolon at the end
- ✅ Exactly 32 characters

**Save and close the file.**

---

## 🎮 Usage

### Running the Application

#### Method 1: Command Line

**Activate virtual environment first (if not already active):**
```powershell
.\venv\Scripts\Activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**Run the app:**
```bash
python main.py
```

#### Method 2: Double-Click Launcher (Windows)

**Create a launcher** (run once):
```powershell
@"
@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python main.py
pause
"@ | Out-File -FilePath WeatherApp.bat -Encoding ASCII
```

**Then double-click `WeatherApp.bat`** to run!

#### Method 3: VS Code

1. Open project folder in VS Code
2. Select Python interpreter (Ctrl+Shift+P → "Python: Select Interpreter" → choose venv)
3. Open `main.py`
4. Click ▶️ Play button (top-right)

---

### Using the Application

1. **Launch the application** using one of the methods above
2. **Enter a city name** in the text box (e.g., "London", "New York", "Tokyo")
3. **Click "Get Weather"** or press **Enter**
4. **View the results:**
   - City name and country
   - Current temperature
   - Weather description
   - "Feels like" temperature
   - Humidity percentage
   - Wind speed
   - Atmospheric pressure

---

## 📁 Project Structure
```
weather-app/
│
├── config/                    # Configuration files
│   ├── __init__.py           # Package initializer
│   └── config.py             # Settings and constants
│
├── src/                      # Source code
│   ├── __init__.py          # Package initializer
│   ├── gui.py               # GUI components (Tkinter)
│   ├── weather_api.py       # API communication logic
│   └── utils.py             # Helper functions
│
├── venv/                     # Virtual environment (not in Git)
│
├── .env                      # Environment variables (not in Git)
├── .gitignore               # Git ignore rules
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── LICENSE                 # MIT License
```

---

## 🔍 How It Works

### Architecture Overview
```
┌─────────────┐
│    User     │
└──────┬──────┘
       │ Enters city name
       ▼
┌─────────────────────────────────────┐
│          GUI (gui.py)               │
│  - Text entry field                 │
│  - Search button                    │
│  - Results display                  │
└──────┬──────────────────────────────┘
       │ Validates input
       ▼
┌─────────────────────────────────────┐
│      Utils (utils.py)               │
│  - Input validation                 │
│  - Data formatting                  │
│  - Error handling                   │
└──────┬──────────────────────────────┘
       │ Valid city name
       ▼
┌─────────────────────────────────────┐
│   Weather API (weather_api.py)      │
│  - Builds API request               │
│  - Sends HTTP request               │
│  - Receives JSON response           │
│  - Parses weather data              │
└──────┬──────────────────────────────┘
       │ API call
       ▼
┌─────────────────────────────────────┐
│   OpenWeatherMap API                │
│  - Processes request                │
│  - Returns weather data             │
└──────┬──────────────────────────────┘
       │ JSON response
       ▼
┌─────────────────────────────────────┐
│   Config (config.py)                │
│  - API key                          │
│  - API endpoints                    │
│  - UI settings                      │
└─────────────────────────────────────┘
```

---

### Data Flow

1. **User Input** → GUI captures city name
2. **Validation** → Utils validates the input
3. **API Request** → Weather API builds and sends request
4. **API Response** → OpenWeatherMap returns JSON data
5. **Data Parsing** → Extract relevant information
6. **Formatting** → Utils formats data for display
7. **Display** → GUI shows formatted weather data

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### ❌ "Invalid API Key" Error

**Possible Causes:**
- API key not activated yet (wait 10-60 minutes after registration)
- Wrong API key copied
- Formatting error in `.env` file

**Solutions:**
1. Check API key status at [OpenWeatherMap API Keys](https://home.openweathermap.org/api_keys)
2. Verify `.env` file format:
```
   WEATHER_API_KEY=your_key_here
```
   (no spaces, no quotes)
3. Copy key again from OpenWeatherMap dashboard

---

#### ❌ "City Not Found" Error

**Possible Causes:**
- Misspelled city name
- City too small (not in database)
- Special characters not supported

**Solutions:**
1. Try major cities first (London, Paris, Tokyo)
2. Use English city names
3. Remove special characters
4. Try adding country code: "Paris,FR"

---

#### ❌ "No Module Named..." Error

**Possible Causes:**
- Virtual environment not activated
- Dependencies not installed
- Wrong Python interpreter

**Solutions:**
1. Activate virtual environment:
```powershell
   .\venv\Scripts\Activate  # Windows
   source venv/bin/activate  # Mac/Linux
```
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Verify Python path:
```bash
   python -c "import sys; print(sys.prefix)"
```
   Should show path with `venv`

---

#### ❌ Window Doesn't Open

**Possible Causes:**
- Tkinter not installed
- Window opening behind other windows
- Display issues

**Solutions:**
1. **Windows:** Reinstall Python with "tcl/tk and IDLE" checked
2. **Linux:**
```bash
   sudo apt-get install python3-tk
```
3. **Mac:** Tkinter included with Python
4. Press Alt+Tab to find window
5. Check task manager for python.exe

---

#### ❌ "Cannot Connect to Weather Service"

**Possible Causes:**
- No internet connection
- Firewall blocking Python
- OpenWeatherMap server down

**Solutions:**
1. Check internet connection
2. Test API in browser:
```
   https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY
```
3. Disable firewall temporarily
4. Check [OpenWeatherMap status](https://status.openweathermap.org/)

---

## 🚀 Future Enhancements

Potential features to add:

- [ ] **5-Day Weather Forecast** - Extended forecast display
- [ ] **Temperature Unit Toggle** - Switch between Celsius/Fahrenheit
- [ ] **Search History** - Remember recent city searches
- [ ] **Favorite Cities** - Save frequently checked cities
- [ ] **Weather Icons** - Visual weather condition icons
- [ ] **Dark Mode** - Theme toggle for dark/light mode
- [ ] **Geolocation** - Auto-detect user's location
- [ ] **Weather Alerts** - Severe weather notifications
- [ ] **Multi-language Support** - Translations
- [ ] **Weather Charts** - Temperature/humidity graphs
- [ ] **Export Data** - Save weather data to file
- [ ] **Offline Mode** - Cache recent searches

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch:**
```bash
   git checkout -b feature/AmazingFeature
```
3. **Make your changes**
4. **Commit your changes:**
```bash
   git commit -m 'Add some AmazingFeature'
```
5. **Push to the branch:**
```bash
   git push origin feature/AmazingFeature
```
6. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide
- Add comments for complex logic
- Update README if adding features
- Test thoroughly before submitting
- Keep commits atomic and well-described

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

---

## 🙏 Acknowledgments

- **[OpenWeatherMap](https://openweathermap.org/)** - For providing the free weather API
- **Python Software Foundation** - For the amazing Python language
- **Tkinter Community** - For GUI framework documentation
- **Stack Overflow Community** - For troubleshooting help
- **GitHub** - For hosting this project

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check the [Troubleshooting](#troubleshooting) section**
2. **Search [existing issues](https://github.com/yourusername/weather-app/issues)**
3. **Create a [new issue](https://github.com/yourusername/weather-app/issues/new)** with:
   - Detailed description
   - Steps to reproduce
   - Error messages
   - Your environment (OS, Python version)

---

## 📊 Project Statistics

- **Lines of Code:** ~500
- **Languages:** Python (100%)
- **API Calls:** OpenWeatherMap v2.5
- **Development Time:** ~2 weeks
- **Last Updated:** January 2025

---

## ⭐ Star This Repository

If you found this project helpful, please consider giving it a star! ⭐

It helps others discover the project and motivates continued development.

---

<div align="center">

**Made with ❤️ and ☕ by [Your Name]**

[⬆ Back to Top](#-weather-application)

</div>
