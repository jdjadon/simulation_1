import datetime
import pandas as pd
from others.global_variable import *
machines = machine_params
job_counter = 0
# Define the job generator function for a specific job type
def job_generator(env, job_type, total_quantity, frequency, lot_size, dispatch_to):
    global job_counter
    while total_quantity > 0:
        quantity = min(total_quantity, lot_size)
        for i in range(quantity):
            # Create a unique ID for each job with job type, generation date, and a unique number
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            job_id = f"{job_type}_{timestamp}_{job_counter}"
            job_counter += 1
            job = {
                "Id" : job_id,
                "type": job_type,
                "time_generated": env.now,
                "operation_done" : 0,
            }

            # Record the generated job
            job_record.append(job)
            if dispatch_to in machines:
                machine = machines[dispatch_to]
                machine.queue.append(job)
            else:
                buffer = buffers[dispatch_to]
                yield buffer.put(job)

        print(f"{env.now}: Generated {quantity} {job_type} jobs and sendto {dispatch_to}")
        total_quantity -= quantity

        yield env.timeout(frequency)




def source(env):
    input_df = pd.DataFrame(input_data)
    for index, row in input_df.iterrows():
        job_type = row["Job Type"]
        total_quantity = row["Total Quantity"]
        frequency = row["Frequency"]
        lot_size = row["Lot Size"]
        dispatch_to = row["Dispatch to"]
        env.process(job_generator(env, job_type, total_quantity, frequency, lot_size, dispatch_to))
