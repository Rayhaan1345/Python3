import requests
import streamlit as st

# api key = 867a0216a489131cfa37409ca09cfc2e

def main():
    z = input("city: ")
    city()
    make_url(z)
    export



def city():
    z = input("enter the location (more detail): ")
    return z

def make_url(z):
    ip = f'http://api.openweathermap.org/data/2.5/weather?q={z}&appid=867a0216a489131cfa37409ca09cfc2e'
    print(ip)
    response = requests.get(ip)
    if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                temp = temp -273
                temp = round(temp)
                desc = data['weather'][0]['description']
                vis = data['visibility']
                coord = data['coord']
                print(f'Temperature: ~{temp} °C')
                print(f'Description: {desc}')
                print(f'Visibility is ~{vis} metres')
                print(f"The co-ordinates of the weather station are: {coord}. Search them up to see the location of monitoring systems!")
    else:
        print('Error fetching weather data')

def export():
      print(make_url)

main()
