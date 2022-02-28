import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")


API_KEY = os.getenv("API_KEY")

GENDER = "Male"
WEIGHT_KG = "225"
HEIGHT_CM = "10.5"
AGE = "30"

APP_ID = APP_ID
API_KEY = API_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
running_data = result['exercises']
sheetly_api = "https://api.sheety.co/4e6a8cda58e39a683e4a2004a9e4fc90/myWorkouts/workouts"

exercise = running_data[0]['name'].title()
duration = running_data[0]['duration_min']
calories = running_data[0]["nf_calories"]

time_day = datetime.now()
insert_date = time_day.strftime('%d''/''%m''/''%Y')
time = time_day.strftime('%X')

sheetly_user = os.getenv("SHEET_USER")
sheetly_pass = os.getenv("SHEETLY_PASS")

workout_data = {
    "workout": {
        "date": insert_date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
send_data = requests.post(url=sheetly_api, json=workout_data,
                          auth=HTTPBasicAuth(sheetly_user, sheetly_pass))

print((send_data.text))
