import simpy
import random


# Define a function to generate random failure and repair times based on a given distribution
def generate_time(distribution, params):
    if distribution == "exponential":
        return random.expovariate(params["failure_rate"])
    elif distribution == "normal":
        return random.normalvariate(params["mean"], params["std_dev"])
    elif distribution == "weibull":
        return random.weibullvariate(params["shape"], params["scale"])
    else:
        return 0  # No failure or repair if distribution not specified


# Define a data structure to store machine parameters
machine_params = {
    "Machine1": {
        "failure_dist": "weibull",
        "repair_dist": "weibull",
        "maintenance_dist": "weibull",
        "shape": 2.0,
        "scale": 1000.0
    },
    "Machine2": {
        "failure_dist": "weibull",
        "repair_dist": "weibull",
        "maintenance_dist": "weibull",
        "shape": 2.0,
        "scale": 1000.0
    },
    # Add more machines with their parameters as needed
}


# Define the machine process as a generator function
def machine(env, name, params, machine_resource):
    failure_dist = params["failure_dist"]
    repair_dist = params["repair_dist"]
    maintenance_dist = params["maintenance_dist"]

    while True:
        # Wait for a job to arrive and request the machine resource
        print(f"{env.now}: {name} is waiting for a job")
        with machine_resource.request() as req:
            yield req

            # Start job processing
            print(f"{env.now}: {name} is processing a job")
            setup_time = random.uniform(1, 3)  # Example setup time distribution
            yield env.timeout(setup_time)

            # Check for failure
            if generate_time(failure_dist, params) > 0:
                print(f"{env.now}: {name} has failed")
                repair_time = generate_time(repair_dist, params)
                yield env.timeout(repair_time)
                print(f"{env.now}: {name} has been repaired")

            # Continue job processing
            process_time = random.uniform(5, 10)  # Example process time distribution
            yield env.timeout(process_time)

            # Check for preventive maintenance
            if generate_time(maintenance_dist, params) > 0:
                print(f"{env.now}: {name} is undergoing preventive maintenance")
                maintenance_duration = generate_time(maintenance_dist, params)
                yield env.timeout(maintenance_duration)
                print(f"{env.now}: {name} maintenance is complete")

        # Release the machine resource
        machine_resource.release


# Create the SimPy environment
env = simpy.Environment()

# Create a resource for each machine
machine_resources = {}
for machine_name, params in machine_params.items():
    machine_resources[machine_name] = simpy.Resource(env, capacity=1)

# Create machine instances with their parameters
machines = {}
for machine_name, params in machine_params.items():
    machines[machine_name] = env.process(machine(env, machine_name, params, machine_resources[machine_name]))


# Generate job arrivals (for demonstration purposes)
def job_generator(env, machines):
    while True:
        machine_name = random.choice(list(machines.keys()))
        machine_resource = machine_resources[machine_name]
        with machine_resource.request() as req:
            yield req
            yield env.timeout(random.uniform(1, 5))  # Time between job arrivals


# Start the job generation process
env.process(job_generator(env, machines))

# Run the simulation
env.run(until=50)  # Adjust the simulation time as needed
