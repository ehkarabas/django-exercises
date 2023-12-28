import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "This field is done"}

get_response = requests.post(
    endpoint,
    json=data,
)

print(f"==>> get_response.json(): {get_response.json()}")
print(f"==>> get_response.status_code: {get_response.status_code}")
