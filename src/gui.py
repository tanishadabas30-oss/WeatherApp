# src/gui.py
import sys
import os
# Ensure parent directory is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox
from config.config import Config
from src.weather_api import get_weather
from src.utils import (
    validate_city_name, format_temperature, capitalize_description,
    format_wind_speed, format_humidity, format_pressure,
    format_city_display, get_weather_emoji
)

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Application")
        self.root.geometry("400x600")
        self.root.configure(bg=Config.BG_COLOR)
        self.root.resizable(False, False)
        
        # Force window to appear on top
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        
        self.city_entry = None
        self.search_button = None
        self.result_frame = None
        self.city_label = None
        self.temp_label = None
        self.feels_like_label = None
        self.description_label = None
        self.humidity_label = None
        self.wind_label = None
        self.pressure_label = None
        
        self.create_widgets()
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root, 
            text="🌤️ Weather App",
            font=("Arial", 24, "bold"),
            bg=Config.BG_COLOR, 
            fg=Config.TEXT_COLOR
        )
        title_label.pack(pady=20)
        
        instruction_label = tk.Label(
            self.root, 
            text="Enter city name:",
            font=("Arial", 12),
            bg=Config.BG_COLOR, 
            fg=Config.TEXT_COLOR
        )
        instruction_label.pack(pady=5)
        
        self.city_entry = tk.Entry(
            self.root, 
            width=30, 
            font=("Arial", 14), 
            justify="center"
        )
        self.city_entry.pack(pady=10)
        self.city_entry.bind("<Return>", lambda event: self.search_weather())
        self.city_entry.focus()
        
        self.search_button = tk.Button(
            self.root, 
            text="Get Weather",
            font=("Arial", 12, "bold"),
            bg=Config.BUTTON_COLOR, 
            fg="white",
            activebackground="#45a049", 
            cursor="hand2",
            command=self.search_weather, 
            width=20, 
            height=2
        )
        self.search_button.pack(pady=10)
        
        self.result_frame = tk.Frame(
            self.root, 
            bg="white", 
            relief=tk.RIDGE, 
            borderwidth=2
        )
        self.result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.result_frame.pack_forget()
        
        self.city_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 18, "bold"),
            bg="white", 
            fg="#1976D2"
        )
        self.city_label.pack(pady=10)
        
        self.temp_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 48, "bold"),
            bg="white", 
            fg="#E65100"
        )
        self.temp_label.pack(pady=5)
        
        self.description_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 16, "italic"),
            bg="white", 
            fg="#424242"
        )
        self.description_label.pack(pady=5)
        
        separator = tk.Frame(
            self.result_frame, 
            height=2, 
            bg="#BDBDBD"
        )
        separator.pack(fill=tk.X, padx=20, pady=10)
        
        self.feels_like_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 12),
            bg="white", 
            fg="#616161"
        )
        self.feels_like_label.pack(pady=2)
        
        self.humidity_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 12),
            bg="white", 
            fg="#616161"
        )
        self.humidity_label.pack(pady=2)
        
        self.wind_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 12),
            bg="white", 
            fg="#616161"
        )
        self.wind_label.pack(pady=2)
        
        self.pressure_label = tk.Label(
            self.result_frame, 
            text="", 
            font=("Arial", 12),
            bg="white", 
            fg="#616161"
        )
        self.pressure_label.pack(pady=2)
    
    def search_weather(self):
        city_name = self.city_entry.get().strip()
        
        is_valid, error_message = validate_city_name(city_name)
        if not is_valid:
            messagebox.showerror("Invalid Input", error_message)
            return
        
        self.search_button.config(text="Loading...", state=tk.DISABLED)
        self.root.update()
        
        result = get_weather(city_name)
        
        if not result['success']:
            messagebox.showerror("Error", result['error'])
            self.search_button.config(text="Get Weather", state=tk.NORMAL)
            return
        
        weather_data = result['data']
        city_display = format_city_display(weather_data['city'], weather_data['country'])
        emoji = get_weather_emoji(weather_data['icon'])
        
        self.city_label.config(text=f"{emoji} {city_display}")
        self.temp_label.config(text=format_temperature(weather_data['temperature'], Config.DEFAULT_UNITS))
        self.description_label.config(text=capitalize_description(weather_data['description']))
        self.feels_like_label.config(text=f"Feels like: {format_temperature(weather_data['feels_like'], Config.DEFAULT_UNITS)}")
        self.humidity_label.config(text=f"💧 Humidity: {format_humidity(weather_data['humidity'])}")
        self.wind_label.config(text=f"💨 Wind: {format_wind_speed(weather_data['wind_speed'], Config.DEFAULT_UNITS)}")
        self.pressure_label.config(text=f"🌡️ Pressure: {format_pressure(weather_data['pressure'])}")
        
        self.result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.search_button.config(text="Get Weather", state=tk.NORMAL)
    
    def run(self):
        self.root.mainloop()