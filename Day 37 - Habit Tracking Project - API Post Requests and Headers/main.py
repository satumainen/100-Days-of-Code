"""
- GET: get data from external system
- POST: send data to an external system
- PUT: update data in an external system
- DELETE: delete data

Project:
- Build a habit tracker using pixela
- https://pixe.la/

HTTP Header
- hides API key in requests or logs

https://pixe.la/v1/users/PIXELA_USERNAME/graphs/books1.html
"""
import os
import requests
import datetime

# Create user account

PIXELA_USERNAME = os.environ.get('PIXELA_USERNAME')
PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
GRAPH_ID = "books1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN, #generated ai key by ourselves, save it
    "username": PIXELA_USERNAME, #generated here
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#notice the new keyword, JSON, used to sen the format above
response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text) #check in text format, json not needed

#create a graph

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Reading Tracker",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

#HTTP header
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers) #headers is a kwarg
#print(graph_response.text)


#post to graph

pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"), #formatting the datetime response
    "quantity": "10",
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(pixel_response.text)


#PUT

date_to_modify = datetime.datetime(year=2025, month=3, day=10).strftime('%Y%m%d')

update_params = {
    "quantity": "5",
    "date": date_to_modify,
}

update_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{date_to_modify}"

update_response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
print(update_response.text)


#DELETE

date_to_modify = datetime.datetime(year=2025, month=3, day=9).strftime('%Y%m%d')

delete_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{date_to_modify}"

delete_response = requests.delete(url=delete_endpoint, headers=headers)
print(delete_response.text)
