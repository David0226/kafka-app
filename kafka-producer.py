from kafka import KafkaProducer
from json import dumps
import time
import sys

def on_send_success(record_metadata):
    print("topic recorded:",record_metadata.topic)
    print("partition recorded:",record_metadata.partition)
    print("offset recorded:",record_metadata.offset)

def on_send_error(excp):
        print(excp)

# 카프카 서버
bootstrap_servers = ["localhost:9092"]

# 카프카 producer 생성
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         key_serializer=None,
                         acks=1,
                         #linger_ms=500,
                         value_serializer=lambda x: dumps(x).encode('utf-8')
                        )

# 카프카 토픽
str_topic_name = 'test'

#produce
for i in range(50):
    response = producer.send(str_topic_name,
                             "test"
                            ).add_callback(on_send_success).add_errback(on_send_error)
    time.sleep(0.5)