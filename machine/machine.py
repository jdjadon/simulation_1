import random
from others.global_variable import *
import simpy
from others.distributions import generate_random_variable

random_ttr = 0
# Define the machine process as a generator function
def machine(env, name, params, machine_resource):
    global random_ttr
    while True:
        machine_params[name]['status'] = 'idle'
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
        setup_time = job_info[job_in["type"]]["operations"][job_in["operation_done"]]["setup_time"]
        machine_params[name]['status'] = 'setup'
        yield env.timeout(setup_time)

        machine_params[name]['status'] = 'process'
        print("{}: {} is processing {}".format(env.now, name, job_in["Id"]))
        process_time = job_info[job_in["type"]]["operations"][job_in["operation_done"]]["process_time"]

        # interruption due to machine failure
        while process_time:
            try:
                start = env.now
                yield env.timeout(process_time)
                process_time = 0
            except simpy.Interrupt:
                print("{} fail".format(name))
                process_time -= env.now - start  # time left for processing the batch
                machine_params[name]['status'] = 'fail'
                yield env.timeout(random_ttr)
                machine_params[name]['status'] = 'process'




def machine_status_f(env, machine_name):
    while True:
        status = str(machine_params[machine_name]['status'])
        machine_status[machine_name][status] = round(machine_status[machine_name][status] + accuracy, 2)
        yield env.timeout(accuracy)


def machine_failure(env, machine_name):
    global random_ttr
    while True:
        for i in machine_params[machine_name]["failure_modes"]:
            condition_met = False
            while not condition_met:
                random_ttf = generate_random_variable(i['failure_dist'], *i['failure_para'])
                random_ttr = generate_random_variable(i['repair_dist'], *i['repair_para'])
                if (random_ttf > 0 and random_ttr > 0):
                    random_ttf = random_ttf + machine_status[machine_name]['process']
                    condition_met = True
        while True:
            if machine_status[machine_name]['process'] < random_ttf:
                yield env.timeout(accuracy)
            elif (machine_params[machine_name]['status'] == 'process'):
                machines[machine_name].interrupt('fails')
                break
            else:
                yield env.timeout(accuracy)



