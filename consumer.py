import json
import time
import random
from kafka import KafkaConsumer

TOPIC = 'qty_updates'

if __name__ == '__main__':
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest'
    )
    for msg in consumer:
        filename = f'{TOPIC}/{int(time.time())}_{random.randint(0, int(time.time()))}.jsonl'
        file1 = open(filename, 'w')
        file1.writelines(msg.value.decode())
        file1.close()
        print('wrote into file: {}'.format(filename))
        print(json.loads(msg.value))