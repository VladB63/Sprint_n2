import allure
import requests
from data import Url, CreateUsers


class UsersMethods:


    @allure.step('Регистрация нового пользователя')
    def new_registration_user(self):
        payload = {
            'email': CreateUsers.EMAIL,
            'password': CreateUsers.PASSWORD,
            'submitPassword': CreateUsers.PASSWORD
        }
        response = requests.post(f'{Url.BASE}{Url.REG}', json=payload)
        return response.status_code, response.json()


    @allure.step('Регистрация нового пользователя с не полными данными')
    def registration_user_fail(self, payload):
        response = requests.post(f'{Url.BASE}{Url.REG}', json=payload)
        return response.status_code, response.json()


    @allure.step('Авторизация пользователя')
    def auth_user(self):
        payload = {
            'email': CreateUsers.EMAIL,
            'password': CreateUsers.PASSWORD
        }
        response = requests.post(f'{Url.BASE}{Url.AUTH}', json=payload)
        return response.status_code, response.json()


    @allure.step('Авторизация пользователя с не полными данными')
    def auth_user_failed(self, payload):
        response = requests.post(f'{Url.BASE}{Url.AUTH}', json=payload)
        return response.status_code, response.json()


