import simpy
import random
from others.distributions import generate_time
from others.global_variable import *


# Define the machine process as a generator function
def machine(env, name, params, machine_resource):
       while True:
        # Wait for a job to arrive and request the machine resource
            print(f"{env.now}: {name} is waiting for a job")

            # check where is the entry point of the machine whether it is machine or buffer and based on it take job from it
            if params["Entry"] in machines:
                entry_point = machines[params["Entry"]]
                # need to make changes that if job is finished in previous machine then only it should pull
                job_in = yield entry_point.get()
            else:
                entry_point = buffers[params["Entry"]]
                job_in = yield entry_point.get()

            print("{}: {} is setting up {}".format(env.now, name, job_in["Id"]))
            setup_time = job_info[job_in["type"]]["operations"][job_in["operation_done"]]["setup_time"]  # Example setup time distribution
            yield env.timeout(setup_time)

            print("{}: {} is processing {}".format(env.now, name, job_in["Id"]))
            process_time = job_info[job_in["type"]]["operations"][job_in["operation_done"]]["process_time"]  # Example setup time distribution
            yield env.timeout(process_time)

            # # Check for failure
            # if generate_time(params["failure_dist"], params["failure_para"]) > 0:
            #     print(f"{env.now}: {name} has failed")
            #     repair_time = generate_time(params["repair_dist"],params["repair_para"])
            #     yield env.timeout(repair_time)
            #     print(f"{env.now}: {name} has been repaired")






#