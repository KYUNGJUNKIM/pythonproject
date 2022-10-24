import time

import requests
from datetime import datetime
import smtplib

PARIS_LAT = 48.856613
PARIS_LNG = 2.352222
MY_MAIL = "jun9894@snu.ac.kr"
PASSWORD = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if (latitude > PARIS_LAT-5 or latitude < PARIS_LAT+5) and (longitude > PARIS_LNG-5 or longitude < PARIS_LNG+5):
        return True


#--------------------------New-----------------------------#
def is_night():
    param = {
        "lat": PARIS_LAT,
        "lng": PARIS_LNG,
        "formatted": 0
    }

    response = requests.get(url=" https://api.sunrise-sunset.org/json", params=param)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
            connection = smtplib.SMTP("jun9894@snu.ac.kr")
            connection.starttls()
            connection.login(MY_MAIL, PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL,
                                msg="Subject: Look UP\n\n Iss is above your head in the Sky")

