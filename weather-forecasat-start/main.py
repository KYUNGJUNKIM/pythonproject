import requests
from datetime import datetime, timedelta

parameters = {
    "lat": 37.5683,
    "lon": 126.9778,
    "exclude": "current,minutely,daily",
    "appid": "2995f17de81e679003f414ff5551135b"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

hour_now = datetime.now().hour
hour_end = (datetime.now() + timedelta(hours=12)).hour
# for _ in range(12):
#     weather = []
#     id_code = data["hourly"][hour_now]["weather"][0]["id"]
#     weather.append(id_code)
#     if id_code < "700":
#         print("Bring an Umbrella before you go outside.")
#     hour_now += 1

rains = False
weather_for_12_hours = data["hourly"][hour_now:hour_end]
for time in weather_for_12_hours:
    condition_code = time["weather"][0]["id"]
    if int(condition_code) < 700:
        rains = True

if rains:
    print("Bring an Umbrella before you go outside.")