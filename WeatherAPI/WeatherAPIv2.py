import requests
import json
import time
from datetime import date


url = "https://weatherapi-com.p.rapidapi.com/forecast.json"


#city = input("Whats the city? ")
#querystring = {"q":{city},"days":"3"}

#headers = {
#	"X-RapidAPI-Key": "d78e25739emsh1ebb038d6fdff39p1ee51fjsn3c022600587c",
#	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
#}
#response = requests.get(url, headers=headers, params=querystring)
#res = response.json()

def get_forecast():
    ## API ##  ## API ##  ## API ##
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q":{city},"days":"3"}
    headers = {
    "X-RapidAPI-Key": "d78e25739emsh1ebb038d6fdff39p1ee51fjsn3c022600587c",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
                }
    response = requests.get(url, headers=headers, params=querystring)
    res = response.json()
    ## API ##  ## API ##  ## API ##

    day_input = int(input("What's the day you want? (max 2 day forecast)"))
    today_day = date.today().day
	
    if   today_day == day_input  :
            day = 0
    elif int(today_day+1) == day_input:
            day = 1
    elif int(today_day+2) == day_input:
            day = 2

    ###DATA###
    #location
    region = res["location"]["name"]
    country = res["location"]["country"]
    #forecast {day}
    last_updated = res["current"]["last_updated"]
    forecast_date = res["forecast"]["forecastday"][day]["date"]
    min_temp_c = res["forecast"]["forecastday"][day]["day"]["mintemp_c"]
    max_temp_c = res["forecast"]["forecastday"][day]["day"]["maxtemp_c"]
    avg_temp_c = res["forecast"]["forecastday"][day]["day"]["avgtemp_c"]
    max_wind_kph = res["forecast"]["forecastday"][day]["day"]["maxwind_kph"]
    totalprecip_mm = res["forecast"]["forecastday"][day]["day"]["totalprecip_mm"]
    avgvis_km = res["forecast"]["forecastday"][day]["day"]["avgvis_km"]
    avg_humidity = res["forecast"]["forecastday"][day]["day"]["avghumidity"]
    chance_of_rain = res["forecast"]["forecastday"][day]["day"]["daily_chance_of_rain"]
    chance_of_snow = res["forecast"]["forecastday"][day]["day"]["daily_chance_of_snow"]
    condition = res["forecast"]["forecastday"][day]["day"]["condition"]["text"]
	
    #PRINTS  
    print(f"\nThe following forecast is from {region}, {country}")
    print(f"The following data was last update at {last_updated}\n")
    print(f"The following data is for {forecast_date}:")
    print(f"- Average temperature: {avg_temp_c}ºC")
    print(f"- Minimum temperature: {min_temp_c}ºC")
    print(f"- Maximum temperature: {max_temp_c}ºC")
    print(f"- Condition: '{condition}'")
    print(f"- Max wind speed: {max_wind_kph}km/h")
    print(f"- Precipitation: {totalprecip_mm}mm")
    print(f"- Chance of rain: {chance_of_rain}%")
    print(f"- Chance of snow: {chance_of_snow}%")
    print(f"- Average humidity: {avg_humidity}%")
    print(f"- Average visibility: {avgvis_km}km\n")

while True:
	### MENU ###
	print("""
#######################################
### Welcome to the Weather Station! ###
#######################################\n""")

	print("1 - Choose a city.")
	print("2 - Check current weather.")
	print("3 - Check forecast for tomorrow.")
	print("4 - Check forecast for after tomorrow.")
	print("5 - Exit.")
	question = input("Choose an option -> ")

	match(question):
		case "1":
			city = input("Whats the city?\n")
			print(f"{city} was defined as the city.\n")
		case "2":
			print("___________________________________________________________") ## ADICIONAR DATA C/ GLOBAL VARIABLE
			get_forecast()
			print("___________________________________________________________")
		case "5":
			print("\nLeaving the Weather Station.")
			time.sleep(0.8)
			print("Leaving the Weather Station..")
			time.sleep(0.8)
			print("Leaving the Weather Station...\n")
			time.sleep(0.5)
			break
		case _:
			print("That's not an option.")
