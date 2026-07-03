import requests

url = "https://dw1nbod1oe.execute-api.us-east-1.amazonaws.com/prod/data"

data = {
 "device_id": "sensor1",
 "temperature": 30,
 "distance": 140,
 "light": 600
}

response = requests.post(url, json=data)

print(response.text)