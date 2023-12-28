import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Abc123"})

print(f"==>> get_response.json(): {get_response.json()}")
print(f"==>> get_response.status_code: {get_response.status_code}")
