# Step 1: Install the required libraries by running the following commands in your terminal:
# pip install streamlit requests

import streamlit as st
import requests

# Step 2: Replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API Key
API_KEY = 'a78526fa98c71a096126f3cf2e3cde22'

# Step 3: Function to fetch temperature data from OpenWeatherMap
def get_temperature(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None  # City not found or other error
    else:
        temperature = data['main']['temp']
        return temperature

# Step 4: Streamlit App for getting the weather
def main():
    # App title
    st.title('Weather App')

    # Input for city name
    city_name = st.text_input('Enter City Name', 'New York')

    # Button to trigger the temperature fetching
    if st.button('Get Temperature'):
        temperature = get_temperature(city_name)
        
        # If temperature is found, display it
        if temperature is not None:
            st.write(f"The current temperature in {city_name} is {temperature}°C.")
        else:
            st.write("City not found or error in fetching weather data. Please try again.")

# Step 5: Run the main function when the script is executed
if __name__ == "__main__":
    main()
