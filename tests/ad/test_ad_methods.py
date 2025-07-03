import allure
import pytest
from data import CreateAd
from tests.conftest import user_registration, log_user
from methods.users_methods import UsersMethods
from methods.ad_methods import AdMethods


class TestAd:

    @allure.title('Проверка успешного создания объявления')
    def test_create_new_ad(self, user_registration, log_user):
        status_code, response = user_registration
        status_code, response = log_user
        token = response['token']['access_token']
        am = AdMethods()
        status_code, response = am.create_new_ad(token)
        assert status_code == 201 and response['id']


    @allure.title('Проверка создания объявления без авторизации')
    def test_create_new_ad_not_auth(self):
        am = AdMethods()
        status_code, response = am.create_new_ad_failed()
        assert status_code == 401



    @allure.title('Проверка редактирования объявления')
    @pytest.mark.parametrize(
        "payload", [
            {'name': CreateAd.NAME,
             'category': 'Авто',
             'condition': 'Новый',
             'city': 'Москва',
             'description': CreateAd.DESCRIPTION,
             'price': CreateAd.PRICE
             }
        ]
    )
    def test_edit_ad(self, payload, user_registration, log_user):
        um = UsersMethods()
        status_code, response = user_registration
        _, response = log_user
        token = response['token']['access_token']
        am = AdMethods()
        _, response = am.create_new_ad(token)
        name_add = response['name']
        id_add = response['id']
        status_code, response = am.edit_ad(token, id_add, name_add, payload)
        assert status_code == 200


    @allure.title('Проверка редактирования не своего объявления')
    @pytest.mark.parametrize(
        "payload", [
            {'name': CreateAd.NAME,
             'category': 'Авто',
             'condition': 'Новый',
             'city': 'Москва',
             'description': CreateAd.DESCRIPTION,
             'price': CreateAd.PRICE
             }
        ]
    )
    def test_edit_not_my(self, payload, user_registration, log_user):
        um = UsersMethods()
        status_code, response = user_registration
        _, response = log_user
        token = response['token']['access_token']
        am = AdMethods()
        status_code, response = am.edit_ad_not_my(token, payload)
        assert status_code == 401 and response == {"message": "Оффер не найден или у вас нет прав на его редактирование",
                                                   "error": "Unauthorized", "statusCode": 401}


    @allure.title('Проверка удаления объявления')
    def test_delete_ad(self, user_registration, log_user):
        status_code, response = user_registration
        _, response = log_user
        token = response['token']['access_token']
        am = AdMethods()
        _, response = am.create_new_ad(token)
        id_add = response['id']
        status_code, response = am.delete_ad(token, id_add)
        assert status_code == 200 and response == {'message': 'Объявление удалено успешно'}







