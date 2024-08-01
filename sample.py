import paho.mqtt.publish as publish

# Define the broker address and port
broker_address = "localhost"
broker_port = 1883

# Define the topic and message you want to publish
topic = "test_topic"
message = "Hello, world!"

# Publish the message to the broker
publish.single(topic, message, hostname=broker_address, port=broker_port)