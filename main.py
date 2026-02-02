# main.py
import sys
import os

# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from src.gui import WeatherApp

def main():
    app = WeatherApp()
    app.run()

if __name__ == "__main__":
    main()