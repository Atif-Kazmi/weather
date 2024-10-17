import streamlit as st
import requests

# OpenWeatherMap API key (replace 'YOUR_API_KEY_HERE' with your actual API key)
API_KEY = 'a78526fa98c71a096126f3cf2e3cde22'

# Predefined list of cities for the dropdown
CITY_LIST = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
    'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
    'Miami', 'Atlanta', 'Boston', 'Seattle', 'Denver', 'Las Vegas',
    'Portland', 'Austin', 'Orlando', 'Minneapolis', 'Detroit'
]

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None  # City not found or other error
    else:
        weather_info = {
            "temperature": data['main']['temp'],
            "condition": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info

# Streamlit App
def main():
    # App title
    st.title('Enhanced Weather App')

    # Dropdown list for selecting the city
    city_name = st.selectbox('Select a City:', CITY_LIST)

    # Button to trigger the weather fetching
    if st.button('Get Weather'):
        weather_data = get_weather_data(city_name)
        
        # If weather data is found, display it
        if weather_data is not None:
            st.write(f"The current temperature in {city_name} is {weather_data['temperature']}°C.")
            st.write(f"Weather Condition: {weather_data['condition'].capitalize()}.")
            st.write(f"Humidity: {weather_data['humidity']}%.")
            st.write(f"Wind Speed: {weather_data['wind_speed']} m/s.")
        else:
            st.write("City not found or error in fetching weather data. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
