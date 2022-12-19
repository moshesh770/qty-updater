import json
import logging

from kafka import KafkaProducer
import os


if os.name == 'nt':
    KAFKA_HOST = "localhost"
else:
    KAFKA_HOST = "kafka"


def serializer(message):
    if not isinstance(message, dict):
        message = message.__dict__
    return json.dumps(message).encode('utf-8')


kafka_producer = KafkaProducer(
    bootstrap_servers=[f'{KAFKA_HOST}:9092'],
    value_serializer=serializer,
    api_version=(0, 10, 1)
)


def send_data(prod):
    message = {'prod_sku': prod.body['_source']['sku'], 'new_qty': prod.body['_source']['inventory']}
    logging.warning('sending data to kafka: %s', message)
    res = kafka_producer.send('qty_updates', message)
    logging.warning('kafka response: %s', res)

