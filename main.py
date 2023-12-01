import simpy
import pandas as pd
import others.userinput
from others import resources
from others.global_variable import *
from source import source
import random

accuracy = 0.1
env = simpy.Environment()

# Create a resource for each machine
machines = resources.add_machine(env)

buffers = resources.add_buffer(env)
source = source.source(env)




job_record_df = pd.DataFrame(job_record)

# Print the job record as a DataFrame
print("Job Generation Record:")
print(job_record_df)




# Run the simulation
env.run(until=100)  # Adjust the simulation time as needed
print(machine_status)
# Convert the list into a DataFrame
global failure_records
failure_records_df = pd.DataFrame(failure_records)

# Display the DataFrame
print(failure_records_df)
import DataVisualisation.visualisation