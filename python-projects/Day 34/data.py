import requests

parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 18,
}
response = requests.get('https://opentdb.com/api.php', params=parameters)
data = response.json()["results"]
print(data)