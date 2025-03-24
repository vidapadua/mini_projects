import requests
from twilio.rest import Client
from apikey import *
from parameters import *


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

def bring_umbrella(param,city_name):
    response = requests.get(OWM_Endpoint, params=param)
    data = response.json()
    # print(data["list"][0]["weather"][0]["id"])

    will_rain = False
    for hour_data in data["list"]:
        # print checks:
        # print(hour_data["dt_txt"])
        # print (condition_code)
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    print(f"\nIn {city_name}:")
    if will_rain:
        print("Bring an umbrella today.")
        print("SMS reminder sent to verified user.")
        client = Client(get_user_account_sid(),get_user_auth_token())
        message = client.messages.create(
            body= "It's going to rain today. Remember to bring an umbrella!",
            from_ = get_user_from_number(),
            to= get_user_verified_calling_number()
        )
        # print(f"SMS sent: {message.sid}")

    else:
        print("It will not rain today according to the forecast.")
        print("No SMS reminder message sent.")


bring_umbrella(toronto_param,"Toronto, Canada")
bring_umbrella(calgary_param, "Calgary,Canada")
bring_umbrella(odense_param,"Odense, Denmark")