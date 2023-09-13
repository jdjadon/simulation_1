import simpy
import random
import pandas as pd
from others.userinput import *

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


# Create the SimPy environment
env = simpy.Environment()

# Define dispatching rules (user-defined)
dispatch_rules = {
    "JobA": "Machine1",
    "JobB": "Machine1",}
    # Add more dispatching rules for other job types

# Create a dataframe for user input
input_data = {
    "Job Type": ["JobA", "JobB"],
    "Total Quantity": [50, 30],
    "Frequency": [3, 5],
    "Lot Size": [5, 10],
}

# Create a list to record generated jobs
job_record = []
machines = machine_params
input_df = pd.DataFrame(input_data)

# Start separate job generator processes for each job type
for index, row in input_df.iterrows():
    job_type = row["Job Type"]
    total_quantity = row["Total Quantity"]
    frequency = row["Frequency"]
    lot_size = row["Lot Size"]
    env.process(job_generator(env, job_type, total_quantity, frequency, lot_size))

# Run the simulation
env.run(until=50)  # Adjust the simulation time as needed
# Create a Pandas DataFrame from the job record
job_record_df = pd.DataFrame(job_record)

# Print the job record as a DataFrame
print("Job Generation Record:")
print(job_record_df)