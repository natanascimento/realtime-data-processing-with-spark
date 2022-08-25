from os.path import abspath, dirname
from os import environ

import dotenv


class Settings:

    dotenv.load_dotenv(dotenv.find_dotenv())

    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))

    APP_PATH = dirname(dirname(dirname(abspath(__file__))))

    KAFKA_BROKER_IP = environ.get('KAFKA_BROKER_IP')
    KAFKA_BROKER_PORT = environ.get('KAFKA_BROKER_PORT')


class KafkaSettings(Settings):

    @property
    def broker(self) -> str:
        return f"{self.KAFKA_BROKER_IP}:{self.KAFKA_BROKER_PORT}"


class KafkaProducerSettings(KafkaSettings):

    @property
    def conf(self) -> dict:
        return {"bootstrap.servers": self.broker}


class KafkaConsumerSettings(KafkaSettings):

    def __init__(self, consumer_group: str):
        self.__consumer_group = consumer_group

    @property
    def conf(self) -> dict:
        return {"bootstrap.servers": self.broker,
                "group.id": self.__consumer_group,
                "auto.offset.reset": "earliest",
                "session.timeout.ms": 6000}
