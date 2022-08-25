from app.core.config import KafkaProducerSettings, KafkaConsumerSettings
from app.events.producer import EventProducer
from app.events.consumer import EventConsumer
from app.events.data import Customer


topic = 'finance.broker.transactions.customers'


def produce():
    for event in range(100):
        EventProducer(kafka_settings=KafkaProducerSettings()) \
            .start(topic=topic,
                   message=Customer().get)


def consume():
    EventConsumer(kafka_settings=KafkaConsumerSettings(consumer_group="fake_consumer_group"))\
        .start(topic=topic)
