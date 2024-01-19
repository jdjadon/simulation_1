import paho.mqtt.client as mqtt
import json

# MQTT Broker Information
broker_address = "127.0.0.1"
broker_port = 1883

# Topic to Subscribe
subscribe_topic = "machine1data"

# Callback when a message is received
# def on_message(client, userdata, msg):
#     print(f"Received message on topic {msg.topic}: {msg.payload.decode('utf-8')}")
#     update_simulation_model(msg.payload.decode('utf-8'))

# Example function to update simulation model
def update_simulation_model(payload):
    machine_data = json.loads(payload)
    # Add logic to update simulation entities based on the received parameters
    # For example, extract values and update corresponding parameters in your simulation model
    print(f"Updating simulation model with machine data: {machine_data}")

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode('utf-8')}")


# Create a MQTT client instance
client = mqtt.Client()

# Set the on_message callback
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Subscribe to the topic
client.subscribe(subscribe_topic)

# Start the loop to receive messages
client.loop_forever()
