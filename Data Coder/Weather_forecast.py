#ACCESSING THE INTERNET WITH PYTHON

#import requests
##
# city_id = "2332453"
#url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}"
#fetch = urllib.request.urlopen(f"{url}")
#data = fetch.read()
#print (data)
#print (type(data))
#print ((data.keys()))
#print (len(data))
#print (data ["message"])
#print (data["cnt"])

#weather_data = data["list"]
#print (type(weather_data))
#print (len (weather_data))

#for i in weather_data:
#   print (i.keys())

#print (weather_data[0]["main"])
#print (weather_data[1]["main"])
#print (weather_data[2]["main"])

#csv_file = open("weather_fcs.csv", "w")

#import requests

#api_key = "8ffa2625543f81542dac585e358a40bc"
#city_id = "2332453"
#url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}"

#fetch = requests.get(f"{url}")
#data = fetch.json()
#city_name = data.get("city").get("name")
#print(data.get("city").get("name"))

#weather_data = data["list"]

#csv_file = open(f"{city_name}.csv", "w")

#print("date", "weather", "Temp", "Humidity", sep = ",", file= csv_file)

#for i in weather_data:
    #print(i["dt_txt"], i["weather"][0]["description"],i["main"]["temp"], i["main"]["humidity"])
   # pass

#csv_file.close()

# modifying the file to ask user to enter city name
import requests
import citylist

def display(city):
    print (city["name"], "--", city["country"])

api_key = "8ffa2625543f81542dac585e358a40bc"
#city_id = "2332453"
cities = citylist.citylist
user_input = input ("Enter city name: ")
matched_data = []
for city in cities:
    if user_input in city["name"]:
        matched_data.append(city)
        display(city)

user_input2 = input ("Please enter country code: ")
for city in matched_data:
    if user_input2.lower() == city["country"].lower():
        city_id = city["id"]

#print (matched_data)
url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}"

fetch = requests.get(f"{url}")
data = fetch.json()
city_name = data.get("city").get("name")
#print(data.get("city").get("name"))

weather_data = data["list"]

csv_file = open(f"{city_name}.csv", "w")

print("date", "weather", "Temp", "Humidity", sep = ",", file= csv_file)

for i in weather_data:
    print(i["dt_txt"], i["weather"][0]["description"],i["main"]["temp"], i["main"]["humidity"])
    print(i["dt_txt"], i["weather"][0]["description"],i["main"]["temp"], i["main"]["humidity"], sep = "," ,file=csv_file)
   # pass

csv_file.close()


