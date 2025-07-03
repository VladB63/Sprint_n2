import allure
import requests
from data import Url, CreateAd
from requests_toolbelt.multipart.encoder import MultipartEncoder


class AdMethods:


    @allure.step('Успешного создание объявления')
    def create_new_ad(self, token):
        payload = MultipartEncoder(
            fields={
                'name': CreateAd.NAME,
                'category': 'Авто',
                'condition': 'Новый',
                'city': 'Москва',
                'description': CreateAd.DESCRIPTION,
                'price': CreateAd.PRICE
            }
        )

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": payload.content_type
        }
        response = requests.post(f'{Url.BASE}{Url.NEW_AD}', headers=headers, data=payload)
        return response.status_code, response.json()

    @allure.step('Создание объявления без авторизации')
    def create_new_ad_failed(self):
        payload = MultipartEncoder(
            fields={
                'name': CreateAd.NAME,
                'category': 'Авто',
                'condition': 'Новый',
                'city': 'Москва',
                'description': CreateAd.DESCRIPTION,
                'price': CreateAd.PRICE
            }
        )
        response = requests.post(f'{Url.BASE}{Url.NEW_AD}', data=payload)
        return response.status_code, response.json()


    @allure.step('Редактирование ранее созданного объявления')
    def edit_ad(self, token, id_add, name, payload):
        response = requests.get(f'{Url.BASE}{Url.AD_SEARCH}', params=name)
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.patch(f'{Url.BASE}{Url.AD_EDIT}{id_add}', headers=headers, json=payload)
        return response.status_code, response.json()


    @allure.step('Редактирование не своего объявления')
    def edit_ad_not_my(self, token, payload):
        response = requests.get(f'{Url.BASE}{Url.ALL_AD}')
        data = response.json()
        id_add = data['offers'][0]['id']
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.patch(f'{Url.BASE}{Url.AD_EDIT}{id_add}', headers=headers, json=payload)
        return response.status_code, response.json()


    @allure.step('Удаление ранее созданного объявления')
    def delete_ad(self, token, id):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.delete(f'{Url.BASE}{Url.AD_DEL}{id}', headers=headers)
        return response.status_code, response.json()




