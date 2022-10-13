import requests
from datetime import datetime

API_KEY = "667feeeab800a9e42e703d71a49b0235"
APP_ID = "03b832b9"
GENDER = "female"
AGE = "21"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/1c2e09dfc4e0cd14a1d373d2c5f844c4/myWorkouts/workouts"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": "70",
    "height_cm": "173",
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
exercises = response.json()["exercises"]
# print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in exercises:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    bearer_headers = {
        "Authorization": "Bearer 37674dsgh65efh"
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

