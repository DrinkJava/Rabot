import requests
from pprint import pprint
import numpy as np
APIKEY = "28e1817908a247be64537e9fa26be3b9"
def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]

def KToF(temp):
	return (9*(temp-273)/5) + 32

def CToF(temp):
	return temp - 273.15
def weather(body):
	ret = ""
	bodyarr = body.split(" ")
	if(len(bodyarr) == 1 or bodyarr[1] == "-H" or bodyarr[1] == "-h"):
		return """Format: :weather location -options
		location can be zip or name of city 
		OPTIONS
		-h: gives help
		-wind: shows wind
		-C: temperature in Celsius
		-K: temperature in Kelvin"""
	city = bodyarr[1]
	data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=" + APIKEY).json()
	if(data["cod"] == 404):
		return "City not found, Try again please"
	ret += "Temperature: "
	if "-C" in bodyarr:
		ret += str(np.round(CToF(data["main"]["temp"])))
	elif "-K" in bodyarr:
		ret += str(np.round(data["main"]["temp"]))
	else:
		ret += str(np.round(KToF(data["main"]["temp"])))
	if "-wind" in bodyarr:
		ret += "\nWind: " + str(np.round(data["wind"]["speed"]*2.23694)) + "mph"
		ret += " in the " + degToCompass(data["wind"]["deg"]) + " direction"
		
	return ret