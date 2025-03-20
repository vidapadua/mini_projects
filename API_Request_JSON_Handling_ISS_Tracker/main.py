import requests

print("Please wait as we fetch the information.\n\n")
response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data=response.json()
longitude=float(data["iss_position"]["longitude"])
latitude=float(data["iss_position"]["latitude"])

iss_position= (longitude,latitude)


parameters= {
    "lat": latitude,
    "lng": longitude,
    "formatted": 1
}

response2=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data2=response2.json()

sunrise_time = data2["results"]["sunrise"]
solar_noon  = data2["results"]["solar_noon"]
sunset_time = data2["results"]["sunset"]



print("The International Space Station (ISS) is humanity's home in space and a research station orbiting about 250 miles above the Earth.")
print(f"Above the sky, the ISS is currently at this coordinates (longitude,latitude): {iss_position}\n")

print("In the same coordinates as the ISS, the following shows the sun is in certain positions.")
print(f"Sunrise Time (UTC): {sunrise_time}")
print(f"Solar Noon (UTC): {solar_noon}")
print(f"Sunset Time (UTC): {sunset_time}")


print("\nTo see the geographic coordinate, You can use this position in a latitude/longitude finder like here https://www.latlong.net.")


