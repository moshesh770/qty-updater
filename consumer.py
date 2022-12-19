import json
from kafka import KafkaConsumer


if __name__ == '__main__':
    consumer = KafkaConsumer(
        'qty_updates',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest'
    )
    for msg in consumer:
        print(json.loads(msg.value))