import json
from kafka import KafkaProducer


def serializer(message):
    if not isinstance(message, dict):
        message = message.__dict__
    return json.dumps(message).encode('utf-8')


kafka_producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=serializer,
    api_version=(0, 10, 1)
)


def send_data(prod):
    kafka_producer.send('qty_updates', {'prod_sku': prod.sku, 'new_qty': prod.qty})
