import requests

city =  input("enter your city")
request = "https://openweathermap.org/api/"+ city

response =  requests.get(request).json()
print(response["weather"])