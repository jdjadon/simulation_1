import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker Information
broker_address = "127.0.0.1"
broker_port = 1883

# Topic to Publish
publish_topic = "machine1data"

# Create a MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Publish machine data
machine_data = {
    "operating_conditions": {
        "speed": 150,
        "load": 75,
        "operator": "John Doe",
        "energy_consumption": 120
    },
    "maintenance_record": {
        "last_maintenance": {
            "type": "Preventive",
            "date": "2023-03-15",
            "details": "Replaced worn-out parts"
        },
        "planned_maintenance": {
            "type": "Scheduled",
            "date": "2023-06-01",
            "details": "Inspect and lubricate moving parts"
        }
    },
    "job_information": {
        "current_job": "JobA",
        "jobs_in_queue": ["JobB", "JobC"],
        "job_sequence": ["JobA", "JobB", "JobC"]
    },
    "failure_modes": [
        {
            "name": "FM1",
            "failure_distribution": "weibull",
            "failure_parameters": [3, 3000],
            "last_failure": {
                "date": "2023-02-20",
                "details": "Bearing failure"
            }
        },
        {
            "name": "FM2",
            "failure_distribution": "exponential",
            "failure_parameters": [5],
            "last_failure": {
                "date": "2023-01-10",
                "details": "Motor failure"
            }
        }
    ]
}

payload = json.dumps(machine_data, ensure_ascii=False).encode('utf-8')
client.publish(publish_topic, payload)
print(f"Published machine data: {payload}")

# Disconnect from the broker

client.loop_forever()