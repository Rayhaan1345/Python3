import requests
import streamlit as st
import sys
import streamlit.components.v1 as components

# api key = 867a0216a489131cfa37409ca09cfc2e
# custom_html = """
# <div class="banner">
#     <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN2jjYufn5KY4HF_-p7PnDGDu0x6h7siQ3a_utKvqk&s" alt="Banner Image">
# </div>
# <style>
#     .banner {
#         width: 100%;
#         height: 250px;
#         overflow: hidden;
#     }
#     .banner img {
#         width: 98%;
#         object-fit: cover;
#     }
# </style>
# """

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
    z = st.text_input("city: (please enter country code for places with same name in multiple regions)", key="main_input", value=None)
    if z is not None:
        prompt5(z)
    city()
    make_url(z)
    export

def prompt5(z):
    op = 5
    while op > 0:
        z = st.text_input("city: (please enter country code for places with same name in multiple regionsUS)", key=op)
        if not z.startswith('a'):
            op -= 1
    if op == 0:
        st.markdown("e")
        sys.exit()
    


def city():
    t = st.text_input("enter the location (more detail)(optional): ")
    return t

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
                #forecast
                #blah = meow.json()
                #forecast_temp = blah['2024-05-01 12:00:00']['temp']
                #forecast_temp = forecast_temp -273
                #forecast_temp = round(forecast_temp)
                #if u:
                   # st.text(f"The expected average temperature for the next 40 days: {forecast_temp}")#


                #Emoji thingie

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

main()
