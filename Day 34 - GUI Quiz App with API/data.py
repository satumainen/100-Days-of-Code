import requests

question_data = []

parameters = {
    "amount": 20,
    "type": "boolean",
    "category" : 18,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
for result in data['results']:
    question_data.append(result)
print(f"Dictionary: {question_data}")
