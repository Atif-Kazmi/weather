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

        # Make the API request to get weather data for the city
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
    st.title('Global Weather App')

    # Input field for the user to type any city name
    city_name = st.text_input('Enter a City Name', '')

    # Button to trigger the weather fetching
    if st.button('Get Weather'):
        if city_name.strip():
            weather_data = get_weather_data(city_name.strip())
            
            if weather_data is not None:
                st.write(f"### Weather in {city_name.capitalize()}:")
                st.write(f"**Temperature**: {weather_data['temperature']}°C")
                st.write(f"**Condition**: {weather_data['condition'].capitalize()}")
                st.write(f"**Humidity**: {weather_data['humidity']}%")
                st.write(f"**Wind Speed**: {weather_data['wind_speed']} m/s")
            else:
                st.error("Unable to retrieve weather for the specified city.")
        else:
            st.warning("Please enter a city name.")

# Run the app
if __name__ == "__main__":
    main()
