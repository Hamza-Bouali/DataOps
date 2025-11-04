from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],  # e.g., host IP or mapped port
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "test-topic"

data = input("enter the event: ")

t = 0
while data!='':
    event = {"event_id": t, "value": data}
    producer.send(topic, value=event)
    data = input("enter the event: ")
    t+=1


producer.flush()
producer.close()
