import requests

# Define API configurations
API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather data for a given city.
    """
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

        print(f"Weather in {city}:")
        print(f"  Description: {weather}")
        print(f"  Temperature: {temp}°C")
        print(f"  Feels like: {feels_like}°C")
        print(f"  Humidity: {humidity}%")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError:
        print("City not found. Please check the city name and try again.")

def main():
    """
    Main application loop.
    """
    print("Welcome to Moon Weather App!")
    while True:
        city = input("Enter the city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
