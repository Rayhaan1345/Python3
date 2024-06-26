import requests
import streamlit as st
import sys
import time
import streamlit.components.v1 as components


components.iframe("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN2jjYufn5KY4HF_-p7PnDGDu0x6h7siQ3a_utKvqk&s", height=150)
## Headers
st.title("Fun, detailed Weather App!")
st.header(":violet[The end of clunky weather apps with the fun and easy to use weather app!]")
st.subheader(":blue[Made by: Rayhaan Khan]")
## for the documentation
url = "https://countrycode.org/"
st.write("For finding country codes visit: [🔘](%s)" % url)

g = st.checkbox("Visibility 👀")
h = st.checkbox("Location coordinates 🌎 🗼 ")
u = st.checkbox("Forecast")
i = st.checkbox("Wind Speed 💨")

def main():
    city_name_key = "city_name_input"
    city_name = st.text_input("city: (please enter country code for places with same name in multiple regions)", key=city_name_key, value=None, on_change=prompt5)
    make_url(city_name)
    export

def prompt5():
    city_name = st.session_state["city_name_input"]
    if not city_name.startswith('a'):        
        st.session_state['num_tries'] = st.session_state['num_tries'] - 1
        st.info(city_name)
        st.info(st.session_state['num_tries'])
        if st.session_state['num_tries'] == 0:
            sys.exit()

def make_url(z):
    ip = f'http://api.openweathermap.org/data/2.5/weather?q={z}&appid=867a0216a489131cfa37409ca09cfc2e'
    zt = f'https://api.openweathermap.org/data/2.5/forecast?q={z}&appid=867a0216a489131cfa37409ca09cfc2e'
    response = requests.get(ip)
    meow = requests.get(zt)
    if response.status_code == 200:
                #current
                data = response.json()
                temp = data['main']['temp']
                temp = temp -273
                temp = round(temp)
                desc = data['weather'][0]['description']
                vis = data['visibility']
                coord = data['coord']
                humid = data['main']['humidity']
                wind = data['wind']
                if i:
                     st.text(f'Wind speed is: {wind} 💨')
                st.text(f'Temperature: ~{temp} °C 🌡️')
                st.text(f"Humidy is: {humid}% 🏝️")

                st.text("The web address for the data: " + ip)

                if desc == 'clear sky':
                     st.markdown(f':green[**Description: {desc} 🌤️**]')
                if desc == 'mist':
                     st.markdown(f':green[**Description: {desc} 🌫️**]')
                if desc == 'smoke':
                     st.markdown(f':green[**Description: {desc} 😶‍🌫️**]')
                if desc == 'broken clouds':
                     st.markdown(f":green[**Description: {desc} 🌥️**]")
                if desc == 'scattered clouds':
                     st.markdown(f':green[**Description: {desc} ⛈️**]')
                if desc == 'light rain':
                     st.markdown(f':green[**Description: {desc} 🌧️**]')
                if desc == 'overcast clouds':
                     st.markdown(f':green[**Description: {desc} ⛈️**]')
                else:
                     st.markdown(f':green[**Description: {desc}**]')

                #check box things
                if g:
                    st.text(f' 👀 Visibility is ~{vis} metres')
                if h:
                    st.text(f" 🌎 The co-ordinates of the weather station are: {coord}. Search them up to see the location of monitoring systems!")
    else:
        st.markdown(" **:red[Error fetching weather data. Maybe you were too specific?]**")


def export():
      st.text(make_url)

if 'num_tries' not in st.session_state:
    st.session_state['num_tries'] = 3
    
main()
