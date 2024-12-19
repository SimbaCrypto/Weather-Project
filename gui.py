import requests
import tkinter as tk
from tkinter import messagebox

# Define API configurations
API_KEY = "your_api_key_here" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather():
    """
    Fetch weather data and update the GUI.
    """
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        # Prepare the API request
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        # Display the weather information
        result_text.set(
            f"Weather in {city}:\n"
            f"  Description: {weather}\n"
            f"  Temperature: {temp}°C\n"
            f"  Feels like: {feels_like}°C\n"
            f"  Humidity: {humidity}%"
        )
    except requests.exceptions.HTTPError:
        result_text.set("City not found. Please try again.")
    except requests.exceptions.RequestException:
        result_text.set("Failed to fetch data. Check your connection.")
    except Exception as e:
        result_text.set(f"An error occurred: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Forecast Application")
root.geometry("400x300")
root.resizable(False, False)

# GUI Elements
tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=fetch_weather)
fetch_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
