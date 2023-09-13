import simpy
from . import *
# Create the SimPy environment
env = simpy.Environment()

# Create machine instances with their parameters
machines = {}
for machine_name, params in userinput.machine_params.items():
    machines[machine_name] = env.process(machine(env, machine_name, params))


# Generate job arrivals (for demonstration purposes)



# Start the job generation process
env.process(job_generator(env, machines))

# Run the simulation
env.run(until=50)  # Adjust the simulation time as needed