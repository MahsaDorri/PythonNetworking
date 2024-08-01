import paho.mqtt.client as mqtt
import json
from assignment4_util import print_data

# Define the MQTT broker address and port
broker_address = "localhost"
broker_port = 1883

# Define the topic to which data will be subscribed
topic = "health_data"

# Define the function to be called when a message is received
def on_message(client, userdata, message):
    # Extract the payload (a JSON string) from the message
    payload = message.payload.decode()
    
    # Convert the JSON string to a dictionary
    data = json.loads(payload)
    
    # Print the dictionary in a human-readable format
    print_data(data)

# Create a client
client = mqtt.Client()

# Assign the on_message delegate to the function defined above
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the specified topic
client.subscribe(topic)

# Print a message indicating that the client is now subscribed to the topic
print(f"Client subscribed to {topic}")

# Start the client's loop to begin receiving messages
client.loop_forever()
