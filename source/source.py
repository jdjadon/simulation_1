import simpy
import random
import pandas as pd
from others.global_variable import *
machines = machine_params

# Define the job generator function for a specific job type
def job_generator(env, job_type, total_quantity, frequency, lot_size):
    while total_quantity > 0:
        quantity = min(total_quantity, lot_size)
        machine_name = dispatch_rules.get(job_type, random.choice(list(machines.keys())))
        machine = machines[machine_name]

        job = {
            "type": job_type,
            "quantity": quantity,
            "exit": machine_name,
            "time_generated": env.now
        }

        # Record the generated job
        job_record.append(job)
        # machine.queue.append(job)

        print(f"{env.now}: Generated {quantity} {job_type} jobs for {machine_name}")

        total_quantity -= quantity

        yield env.timeout(frequency)




def source(env):
    input_df = pd.DataFrame(input_data)
    for index, row in input_df.iterrows():
        job_type = row["Job Type"]
        total_quantity = row["Total Quantity"]
        frequency = row["Frequency"]
        lot_size = row["Lot Size"]
        env.process(job_generator(env, job_type, total_quantity, frequency, lot_size))
