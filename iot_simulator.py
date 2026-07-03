import requests
import random
import time
from datetime import datetime

API_URL = "https://dw1nbod1oe.execute-api.us-east-1.amazonaws.com/prod/data"

def generate_data():
    return {
        "device_id": "sensor_" + str(random.randint(1,5)),
        "temperature": round(random.uniform(20,40),2),
        "distance": random.randint(10,200),
        "light": random.randint(100,900),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:

    data = generate_data()

    print("Sending:", data)

    try:
        response = requests.post(API_URL, json=data)
        print("Response:", response.text)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)