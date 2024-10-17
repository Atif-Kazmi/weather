import streamlit as st
import requests
import os

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city_name):
    try:
        # Get the API key from environment variables or prompt the user if not set
        api_key = os.getenv('OPENWEATHER_API_KEY')
        if not api_key:
            st.error("API Key not set. Please set 'OPENWEATHER_API_KEY' environment variable.")
            return None

        # Make the API request
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Handle API errors (like invalid city)
        if data.get("cod") != 200:
            st.error(f"Error fetching data: {data.get('message', 'Unknown error')}")
            return None

        # Parse weather data
        weather_info = {
            "temperature": data['main']['temp'],
            "condition": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info
    except Exception as e:
        st.error(f"Failed to retrieve weather data: {str(e)}")
        return None

# Streamlit App
def main():
    st.title('Enhanced Weather App')

    # Predefined list of cities for the dropdown (could be expanded or fetched dynamically)
    CITY_LIST = [
        'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
        'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
        'Miami', 'Atlanta', 'Boston', 'Seattle', 'Denver', 'Las Vegas',
        'Portland', 'Austin', 'Orlando', 'Minneapolis', 'Detroit'
    ]

    # Dropdown list for selecting t
