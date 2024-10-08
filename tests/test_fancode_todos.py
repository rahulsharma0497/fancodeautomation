import pytest
from utils.api_utils import get_users, get_todos

@pytest.fixture(scope="module")
def base_url():
    return "http://jsonplaceholder.typicode.com"

def is_fancode_city(user):
    """Check if user is in the FanCode city based on lat/long coordinates."""
    lat = float(user['address']['geo']['lat'])
    long = float(user['address']['geo']['lng'])
    return -40 <= lat <= 5 and 5 <= long <= 100

def test_fancode_user_tasks(base_url):
    """Verify that  50% tasks completed."""
    users = get_users(base_url)
    todos = get_todos(base_url)

    # Filter FanCode users
    fancode_users = [user for user in users if is_fancode_city(user)]

    for user in fancode_users:
        user_todos = [todo for todo in todos if todo['userId'] == user['id']]
        if user_todos:
            completed_tasks = sum(1 for todo in user_todos if todo['completed'])
            completion_percentage = (completed_tasks / len(user_todos)) * 100

            assert completion_percentage > 50, f"User {user['id']} has less than 50% tasks completed."
