import requests
import datetime as dt
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
username = "YOUR USERNAME"
token = "YOUR TOKEN"

#USER
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
# GRAPH
graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
graph = "graph1"
graph_config = {
    "id": graph,
    "color": "shibafu",
    "type": "int",
    "unit": "commit",
    "name": "Coding challenge graph"
}
headers = {
    "X-USER-TOKEN": token,
}

#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = dt.datetime(year=2023, month=8, day=20)
today = today.strftime("%Y%m%d")
print(today)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph}/{today}"

pixel_body = {

    "quantity": "10"
}

# PIXEL
response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)

