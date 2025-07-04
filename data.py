import random
import string

class Url:
    BASE = 'https://qa-desk.stand.praktikum-services.ru/api/'
    REG = 'signup'
    AUTH = 'signin'
    NEW_AD = 'create-listing'
    AD_SEARCH = 'offers/1/'
    AD_EDIT = 'update-offer/'
    AD_DEL = 'listings/'
    ALL_AD = "listings/1"


class CreateUsers:

    EMAIL = f"BoardUser{random.randint(1000, 100000)}@ya.ru"
    PASSWORD = str(random.randint(10, 100))


class CreateAd:

    NAME = f"Тест - {random.randint(1, 100000)}"
    DESCRIPTION = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    PRICE = str(random.randint(10, 100))