import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(f"Response Code: {response.status_code}\n")
response.raise_for_status()

data=response.json()
longitude=float(data["iss_position"]["longitude"])
latitude=float(data["iss_position"]["latitude"])

iss_position= (longitude,latitude)
print("The International Space Station (ISS) is humanity's home in space and a research station orbiting about 250 miles above the Earth.")
print(f"Above the sky, the ISS is currently at this coordinates (longitude,latitude): {iss_position}")
print("\nTo see the geographic coordinate, You can use this position in a latitude/longitude finder like here https://www.latlong.net.")

parameters= {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0
}

response2=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data2=response2.json()
print(data2)

sunrise_time = data2['results']['sunrise']
sunrise_date = sunrise_time.split("T")[0]
sunrise_hour = int(sunrise_time.split("T")[1].split(":")[0])
print(sunrise_date,sunrise_hour)

