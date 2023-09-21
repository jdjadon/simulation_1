import simpy
import pandas as pd
import others.userinput
from others import resources
from others.global_variable import *
from source import source
import random


env = simpy.Environment()

# Create a resource for each machine
machines = resources.add_machine(env)
source = source.source(env)
buffers = resources.add_buffer(env)



job_record_df = pd.DataFrame(job_record)

# Print the job record as a DataFrame
print("Job Generation Record:")
print(job_record_df)




# Run the simulation
env.run(until=50)  # Adjust the simulation time as needed
