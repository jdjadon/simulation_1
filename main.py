import simpy
import pandas as pd
import others.userinput
from others import resources, initialisation
from others.global_variable import *
from source import source
from DataVisualisation import visualisation
import random


accuracy = 0.1
env = simpy.Environment()

# Create a resource for each machine
resources.add_machine(env)
resources.add_buffer(env)
source.source(env)
job_record_df = pd.DataFrame(job_record)
# print(buffer_params)
env.process(initialisation.buffer_initial(env, buffer_params))
initialisation.machine_initial(env, machine_params)

# Print the job record as a DataFrame
print("Job Generation Record:")
print(job_record_df)
# Run the simulation
env.run(until=5)  # Adjust the simulation time as needed
# print(machine_status)
# Convert the list into a DataFrame
for key, values in buffers.items():
    print(values.items)
global failure_records
failure_records_df = pd.DataFrame(failure_records)

# Display the DataFrame
# print(failure_records_df)
# visualisation.machine_timeline(timeline_logs)
