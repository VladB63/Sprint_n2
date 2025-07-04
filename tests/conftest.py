import pytest
import requests
from data import Url, CreateUsers

@pytest.fixture
def user_registration():
    payload = {
        'email': CreateUsers.EMAIL,
        'password': CreateUsers.PASSWORD,
        'submitPassword': CreateUsers.PASSWORD
    }
    response = requests.post(f'{Url.BASE}{Url.REG}', json=payload)
    return response.status_code, response.json()



@pytest.fixture
def log_user():
    payload = {
        'email': CreateUsers.EMAIL,
        'password': CreateUsers.PASSWORD
    }
    response = requests.post(f'{Url.BASE}{Url.AUTH}', json=payload)
    return response.status_code, response.json()