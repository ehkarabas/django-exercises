import requests

from getpass import getpass

auth_endpoint_token = "http://localhost:8000/api/auth/"
auth_endpoint_jwt = "http://localhost:8000/api/token/"

username = input("Username:\n")
password = getpass("Password:\n")
data = {"username": username, "password": password}


auth_response = requests.post(auth_endpoint_jwt, json=data)

print(f"==>> auth_response.json(): {auth_response.json()}")
print(f"==>> auth_response.status_code: {auth_response.status_code}")


if auth_response.status_code == 200:
    token = auth_response.json().get("access")
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "http://localhost:8000/api/products"

    data = {"title": "This field is done", "price": 33}

    get_response = requests.get(
        endpoint,
        headers=headers,
    )

    data = get_response.json()
    next_url = data["links"]["next"]

    while next_url is not None:
        get_response = requests.get(
            next_url,
            headers=headers,
        )
        data = get_response.json()
        next_url = data["links"]["next"]
        print(f"==>> get_response.json(): {get_response.json()}")
        print(f"==>> get_response.status_code: {get_response.status_code}")
