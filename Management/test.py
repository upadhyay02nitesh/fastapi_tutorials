import requests

response = requests.get(
    "http://127.0.0.1:8000/resource",
    headers={"user-id": "user_1"}
)
print(response.json())
