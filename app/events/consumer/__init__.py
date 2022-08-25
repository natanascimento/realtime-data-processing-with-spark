from app.core.config import KafkaConsumerSettings
from confluent_kafka import Consumer, KafkaException


class EventConsumer:

    def __init__(self, kafka_settings: KafkaConsumerSettings):
        self.__consumer = Consumer(kafka_settings.conf)

    @staticmethod
    def __print_assignment(consumer, partitions):
        print('Assignment:', partitions)

    def start(self, topic: str):
        self.__consumer.subscribe([topic], on_assign=self.__print_assignment)

        try:
            while True:
                msg = self.__consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())
                else:
                    print(f'{msg.topic()} [{msg.partition()}] at offset {msg.offset()} with key {str(msg.key())}:\n')
                    print(msg.value())
        except KeyboardInterrupt:
            print("Aborted by user\n")
        finally:
            self.__consumer.close()
