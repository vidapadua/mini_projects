import requests
from apikey import get_user_api_key

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

calgary_param={
    "lat":51.0460954,
    "lon":-114.065465,
    "appid": get_user_api_key() #API Key Generated
}

odense_param={
    "lat":55.3997225,
    "lon":10.3852104,
    "appid": get_user_api_key()
}


ca_response=requests.get(OWM_Endpoint, params=calgary_param)
ca_data=ca_response.json()
print(ca_data)

dk_response=requests.get(OWM_Endpoint, params=odense_param)
dk_data=dk_response.json()