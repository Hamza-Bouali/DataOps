from kafka import KafkaConsumer
import json

def safe_deserializer(v):
    if v is None:
        return None
    try:
        return json.loads(v.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Warning: could not decode message value: {v!r}, error: {e}")
        return None

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:29092'],
    group_id='my_consumer_group',
    auto_offset_reset='earliest',
    value_deserializer=safe_deserializer
)

print("Listening for messages on topic 'test-topic' …")

for message in consumer:
    print(f"Received: topic={message.topic} partition={message.partition} offset={message.offset}")
    print("  key =", message.key)
    print("  value =", message.value)