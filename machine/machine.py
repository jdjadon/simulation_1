import simpy
import random
from others.distributions import generate_time
from others.global_variable import *


# Define the machine process as a generator function
def machine(env, name, params, machine_resource):
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
            if generate_time(params["failure_dist"], params["failure_para"]) > 0:
                print(f"{env.now}: {name} has failed")
                repair_time = generate_time(params["repair_dist"],params["repair_para"])
                yield env.timeout(repair_time)
                print(f"{env.now}: {name} has been repaired")

            # Continue job processing
            process_time = random.uniform(5, 10)  # Example process time distribution
            yield env.timeout(process_time)

        # Release the machine resource
        machine_resource.release


#