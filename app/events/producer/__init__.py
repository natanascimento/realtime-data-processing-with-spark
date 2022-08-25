from confluent_kafka import Producer
from app.core.config import KafkaSettings


class EventProducer:

    def __init__(self, kafka_settings: KafkaSettings):
        self.__producer = Producer(**kafka_settings.conf)

    @staticmethod
    def __delivery_callback(error, msg) -> None:
        if error:
            print(f'Message failed delivery: {error}\n')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}] @ {msg.offset()}\n')

    def produce(self, topic: str, message: dict) -> None:
        try:
            self.__producer.produce(topic, str(message), callback=self.__delivery_callback)
            self.__producer.poll(0)
        except BufferError:
            print(f'Local producer queue is full ({len(self.__producer)} messages awaiting delivery): try again\n')
        except Exception as exception:
            print(exception)

        self.__producer.flush()
