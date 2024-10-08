import requests

def get_users(base_url):
    """Fetch all users from the API"""
    response = requests.get(f"{base_url}/users")
    response.raise_for_status()
    return response.json()

def get_todos(base_url):
    """Fetch all todos from the API"""
    response = requests.get(f"{base_url}/todos")
    response.raise_for_status()
    return response.json()
