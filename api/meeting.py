import requests
import json

API_KEY = "microtalk_default_secret"

MICROTALK_URL = "https://mirotalk.up.railway.app/api/v1/meeting"

headers = {
    "authorization": API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(
    MICROTALK_URL,
    headers=headers
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("meeting:", data["meting"])