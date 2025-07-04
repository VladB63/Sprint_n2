import allure
import pytest
from data import CreateUsers
from methods.users_methods import UsersMethods

class TestUserMethods:

    @allure.title('Проверка успешной регистрации нового пользователя')
    def test_reg_new_user(self):
        um = UsersMethods()
        status_code, response = um.new_registration_user()
        assert status_code == 201 and response['access_token']

    @allure.title('Проверка регистрации дубля нового пользователя')
    def test_reg_new_user_dubl(self):
        um = UsersMethods()
        um.new_registration_user()
        um.new_registration_user()
        status_code, response = um.new_registration_user()
        assert status_code == 400 and response == {'message': 'Почта уже используется',
                                                   'statusCode': 400}

    @allure.title('Проверка неуспешной регистрации нового пользователя')
    @pytest.mark.parametrize(
        "payload", [
            {'email': '', 'password': '', 'submitPassword': ''},
            {'email': '', 'password': CreateUsers.PASSWORD, 'submitPassword': CreateUsers.PASSWORD},
            {'email': '', 'password': CreateUsers.PASSWORD, 'submitPassword': ''}
        ]
    )
    def test_reg_new_user_failed(self, payload):
        um = UsersMethods()
        status_code, response = um.registration_user_fail(payload)
        assert status_code == 400 and response == {'message': ['error: Не валидный Email'],
                                                   'statusCode': 400}


    @allure.title('Проверка успешной авторизации пользователя')
    def test_auth_user(self):
        um = UsersMethods()
        um.new_registration_user()
        status_code, response = um.auth_user()
        assert status_code == 201 and response['token']


    @allure.title('Проверка неуспешной авторизации пользователя')
    @pytest.mark.parametrize(
        "payload", [
            {'email': CreateUsers.EMAIL, 'password': ''},
            {'email': '', 'password': CreateUsers.PASSWORD}
        ]
    )
    def test_auth_user_failed(self, payload):
        um = UsersMethods()
        um.new_registration_user()
        status_code, response = um.auth_user_failed(payload)
        assert status_code == 404 and response == {'message': 'Логин или пароль неверны',
                                                   'statusCode': 404}