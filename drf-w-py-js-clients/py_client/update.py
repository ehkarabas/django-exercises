import requests

endpoint = "http://localhost:8000/api/products/1/update"

data = {"title": "This field has changed again", "price": 5443}

get_response = requests.patch(endpoint, json=data)

print(f"==>> get_response.json(): {get_response.json()}")
print(f"==>> get_response.status_code: {get_response.status_code}")
