import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


USERNAME = os.getenv('USER_NAME')
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph = f"https://pixe.la/v1/users/{USERNAME}/graphs"
print(pixela_graph)

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": "yes"}

# create_username = requests.post(url=pixela_graph, json=parameters)
# print(create_username.text)


# create a new graph

header = {
    "X-USER-TOKEN": TOKEN
}

graph = {
    "id": "graph1",
    "name": "cycling",
    "unit": 'Km',
    "type": "float",
    "color": 'ajisai'}

# create_graph = requests.post(url=pixela_endpoint, json=graph, headers=header)
# print(create_graph.text)


# create a new entry to out graph

create_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
today = datetime(year=2022, month=2, day=20)
create_pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"}

response = requests.post(url=create_pixel_endpoint,
                         json=create_pixel_body, headers=header)
print(response.text)

# update the pixel entry  on the graph
date = '20220227'
update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date}"
udate_body = {
    "quantity": '5'
}

# update_entry = requests.put(url=update_endpoint, headers=header, json=udate_body)
#
# print(update_entry.text)
