import paho.mqtt.client as mqtt
import json
import time
from assignment4_util import create_data, print_data

# Define the MQTT broker address and port
broker_address = "localhost"
broker_port = 1883

# Define the topic to which data will be published
topic = "health_data"

# Create a client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Loop to publish multiple payloads
for i in range(3):
    # Create a dictionary containing sample data
    data = create_data()
    
    # Convert the dictionary to a JSON string
    payload = json.dumps(data)
    
    # Publish the JSON string to the specified topic
    client.publish(topic, payload)
    
    # Print a message indicating that the data has been published
    print(f"Data {data['id']} published to {topic}")
    
    # Sleep for 5 seconds before publishing the next payload
    time.sleep(5)

# Disconnect from the MQTT broker
client.disconnect()
