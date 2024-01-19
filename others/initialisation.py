import json
import os
from others.global_variable import *

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
machine_json_file_path = os.path.join(root_directory, "machine.json")
buffer_json_file_path = os.path.join(root_directory, "buffer.json")

def buffer_initial(env, buffer_params):
    with open(buffer_json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    count = 0
    for key, values in buffer_params.items():
        initial_contents = json_data.get(key.lower(), {}).get("current_status", {})
        buffer = buffers[key]
        for item, quantity in initial_contents.items():
            for i in range(quantity):
                timestamp = env.now
                job_id = f"{item}_{timestamp}_i{count}"
                count += 1
                job = {
                    "Id": job_id,
                    "type": item,
                    "time_generated": 0,
                    "operation_done": 0,
                    # You may need to add more parameters as needed
                }
                # Assuming key is a SimPy store, put the job into the buffer
                yield buffer.put(job)
    return


def machine_initial(env, machine_params):
    with open(machine_json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    for key, values in machine_params.items():
        timestamp = env.now
        item = json_data[key]["job_information"]['current_job']
        job_id = f"{item}_{timestamp}_{key}"
        job = {
            "Id": job_id,
            "type": item,
            "time_generated": 0,
            "operation_done": 0,
            # You may need to add more parameters as needed
        }
        machine_params[key]["current_job"] = job
        machine_params[key]["status"] = json_data[key]["job_information"]['status']
        machine_params[key]["process_time_completed"] = json_data[key]["job_information"]['process_time_completed']
    return