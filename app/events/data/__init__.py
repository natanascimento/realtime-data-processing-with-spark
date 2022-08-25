from datetime import datetime
from uuid import uuid4

from faker import Faker


class Customer:

    def __init__(self):
        self.__fake = Faker()
        self.__customer_id = str(uuid4())
        self.__profile = self.__fake.simple_profile()
        self.__customer_name = self.__profile['name']
        self.__customer_username = self.__profile['username']
        self.__customer_gender = self.__profile['sex']
        self.__customer_address = self.__profile['address'].replace('\n', ' - ')
        self.__customer_buy_price = self.__fake.pricetag()
        self.__customer_country = self.__fake.country()
        self.__createdAt = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    @property
    def get(self) -> dict:
        customer = {"customer_id": self.__customer_id,
                    "customer_username": self.__customer_username,
                    "customer_name": self.__customer_name,
                    "customer_gender": self.__customer_gender,
                    "customer_address": self.__customer_address,
                    "customer_purchase_price": self.__customer_buy_price,
                    "customer_country": self.__customer_country,
                    "createdAt": self.__createdAt}

        return customer
