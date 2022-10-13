import requests
from datetime import datetime
PIXELA_END_POINT = "https://pixe.la/v1/users"
USERNAME = "tasnimtantawi"
TOKEN = "h4794hwjdwshgewj3k4i83j4"
GRAPH_ID = "graph1"
today = datetime.now()

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_end_point = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
print(response.text)
pixel_creation_end_point = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}
response = requests.post(url=pixel_creation_end_point, json=pixel_config, headers=headers)

# update_end_point = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "3.5"
}
# response = requests.put(url=pixel_creation_end_point, json=update_config, headers=headers)
