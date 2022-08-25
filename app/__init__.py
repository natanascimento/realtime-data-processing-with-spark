from app.core.config import KafkaSettings
from app.events.producer import EventProducer

topic = 'finance.broker.transactions.customers'

message = {"customer_first_name": "Natan",
           "customer_last_name": "Nascimento",
           "customer_age": "23"}


def produce():
    for i in range(10):
        EventProducer(kafka_settings=KafkaSettings())\
            .produce(topic=topic,
                     message=message)


def consume():
    print("CONSUMING DATA ...")
