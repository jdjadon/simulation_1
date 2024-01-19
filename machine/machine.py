import random
from others.global_variable import *
import simpy
from others.distributions import generate_random_variable


# Define the machine process as a generator function
def machine(env, name, params, machine_resource):

    while True:
        print(f"{env.now}: {name} is waiting for a job")
        # check where is the entry point of the machine whether it is machine or buffer and based on it take job from it
        while machine_params[name]['current_job'] == "NULL":                                    #run until machine gets the job either by push or pull mechanism
            if params["Entry"] in machines:
                # if entry point is machine then chk that machine for input
                if machine_params[params["Entry"]]['status'] == "PostProcessing:":               # take only if previous machine has finished operation
                    entry_point = machines[params["Entry"]]
                    job_in = yield entry_point.get()
                    machine_params[name]['current_job'] = job_in
                    machine_params[params["Entry"]]['status'] = 'idle'
                    machine_params[params["Entry"]]['current_job'] = 'NULL'
                else:
                    yield env.timeout(accuracy)

            elif params["Entry"] in buffers:
                try:
                    entry_point = buffers[params["Entry"]]
                    job_in = yield entry_point.get()
                    machine_params[name]['current_job'] = job_in
                except:
                    yield env.timeout(accuracy)

        job_in = machine_params[name]['current_job']                                            # when pushed by other machine in this machine
        if machine_params[name]['status'] == "idle" :
            print("{}: {} is setting up {}".format(env.now, name, job_in["Id"]))
            setup_time = job_info[job_in["type"]]["operations"][job_in["operation_done"]]["setup_time"]
            machine_params[name]['status'] = 'setup'
            yield env.timeout(setup_time)
            machine_params[name]['status'] = 'process'

        if machine_params[name]['status'] == "process" :
            print("{}: {} is processing {}".format(env.now, name, job_in["Id"]))
            process_time = job_info[job_in["type"]]["operations"][job_in["operation_done"]]["process_time"] - machine_params[name]['process_time_completed']

            # interruption due to machine failure
            while process_time:
                try:
                    start = env.now
                    yield env.timeout(process_time)
                    process_time = 0
                except simpy.Interrupt:
                    print("{} failed".format(name))
                    process_time -= env.now - start  # time left for processing the batch
                    machine_params[name]['status'] = 'fail'
                    global failure_records
                    yield env.timeout(round(failure_records[-1]["TimeToRepair"],1))
                    print("{} Repaired".format(name))
                    machine_params[name]['status'] = 'process'
            job_in["operation_done"] += 1
            print(machine_params[name]['current_job'])
            machine_params[name]['status'] = 'PostProcessing'
        # if exit is defined in next machine
        while machine_params[name]['current_job'] != "NULL" :
            # it means there is job present at the machine
            exit_point = params["Exit"]
            if params["Exit"] in machines:                                                # next machine should be idle state to put a job into it
                if machine_params[params["Exit"]]['status'] == 'idle':
                    machine_params[params["Exit"]]['current_job'] = job_in
                    machine_params[name]['current_job'] = "NULL"                          # now there is no job on machine
                    machine_params[name]['status'] = 'idle'                               # machine status changed to idle

                                    # next machine got the job

                else:
                    machine_params[name]['status'] = 'blocked'                            # machine is blocked wait till machine exit machine status changes.
                    yield env.timeout(accuracy)

            elif params["Exit"] in buffers:
                #need to add that when buffer is full it shows blocked and wait
                yield buffers[exit_point].put(job_in)                                                  # job pushed to the buffer
                machine_params[name]['current_job'] = "NULL"                              # there is no job on the machine
                machine_params[name]['status'] = 'idle'
                # machine_params[params["Exit"]]['current_job'] = job_in need to incease buffer count

            else:                                                                          # exit point is not defined by the user
                yield env.timeout(accuracy)
                # wait until job is pulled by some other asset





def machine_status_f(env, machine_name):
    while True:
        status = str(machine_params[machine_name]['status'])
        machine_status[machine_name][status] = machine_status[machine_name][status] + accuracy
        global timeline_logs
        # Update the timeline log
        if machine_name not in timeline_logs:
            timeline_logs[machine_name] = {'Time': [], 'Status': []}
        timeline_logs[machine_name]['Time'].append(round(env.now,2))
        timeline_logs[machine_name]['Status'].append(status)
        yield env.timeout(accuracy)



def machine_failure(env, machine_name, failure_mode):
    while True:
        condition_met = False
        while not condition_met:
            random_ttf = generate_random_variable(failure_mode['failure_dist'], *failure_mode['failure_para'])
            random_ttr = generate_random_variable(failure_mode['repair_dist'], *failure_mode['repair_para'])
            if (random_ttf > 0 and random_ttr > 0):
                ttf = random_ttf + machine_status[machine_name]['process']
                failure_mode["ttf"] = ttf
                failure_mode["ttr"] = random_ttr
                condition_met = True
        while True:
            if machine_status[machine_name]['process'] < ttf:
                yield env.timeout(accuracy)
            elif (machine_params[machine_name]['status'] == 'process'):
                machines[machine_name].interrupt('fails')
                # Update failure records DataFrame
                # Update failure records DataFrame
                global failure_records
                failure_records.append({
                    'MachineName': machine_name,
                    'FailureMode': failure_mode['name'],
                    "failureTime" : env.now,
                    'TimeToFailure': random_ttf,
                    'TimeToRepair': random_ttr # Initially set repair time to None
                })
                break
            else:
                yield env.timeout(accuracy)



