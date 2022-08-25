from confluent_kafka import Producer
import sys

conf = {'bootstrap.servers': 'localhost:9092'}

topic = 'finance.broker.transactions.customers'


def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                         (msg.topic(), msg.partition(), msg.offset()))


def produce():
    print("PRODUCING DATA ...")

    p = Producer(**conf)

    try:
        # Produce line (without newline)
        p.produce(topic, "teste", callback=delivery_callback)

    except BufferError:
        sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                         len(p))

    p.poll(0)
    p.flush()

def consume():
    print("CONSUMING DATA ...")
