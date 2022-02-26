
import requests
from datetime import datetime
import smtplib

MY_LAT = 40.661930
MY_LONG = -74.211647


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude < - MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG:
        return True


def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True


if is_overhead() and is_dark():
    email = 'samplemail@gmail.com'
    password = 'password123'
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(to_addrs=email, from_addr=email,
                            msg='Subject: Internatinal Station Alert\n\n Check the sky')
