'''
This program uses a public Google Maps api key and the Weather Underground API Key to determine the
current PM2.5 values for a given location. 
does things with pm2.5 and aqi
'''

from json import dumps
from requests import get
import random

#get the users location
city = raw_input("Enter the City: ")
state = raw_input("Enter the State (CT Format): ")
location_url='https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '+' + state + '&key=AIzaSyDnT5Gx-2_Xtv3-hhybSNuljyzOh55R0Ck'

json_location = get(location_url).json()
url_lat = json_location['results'][0]['geometry']['location']['lat']
url_lng = json_location['results'][0]['geometry']['location']['lng']

string_lat = str(url_lat)
string_long = str(url_lng)



#call pm2.5 values based on the lat/long of the users entered city

url = 'https://api.darksky.net/forecast/ec17a58a0a683d7f18027afc8e878269/' + string_lat +',' + string_long
json_data = get(url).json()

sumamry_daily = json_data['daily']['summary']

print sumamry_daily

with open('output.json', 'w') as ofile:
    ofile.write(dumps(sumamry_daily))
ofile.close()