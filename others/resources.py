import simpy
from others.global_variable import *
from machine import machine


def add_machine(env):   
    for machine_name, params in machine_params.items():
        machine_resources[machine_name] = simpy.Resource(env, capacity=1)
    for machine_name, params in machine_params.items():
        machines[machine_name] = env.process(
            machine.machine(env, machine_name, params, machine_resources[machine_name]))
        machine_status.update({
                            machine_name : {
                            'idle': 0,
                          'process': 0,
                          'setup': 0,
                          'fail': 0,
                          'maintainence': 0,
                            'blocked': 0,
                            "PostProcessing" : 0}})
        env.process(machine.machine_status_f(env, machine_name))

        for failure_mode in machine_params[machine_name]["failure_modes"]:
            env.process(machine.machine_failure(env, machine_name, failure_mode))
    return machine_resources, machines

def add_buffer(env):
    for buffer_name, params in buffer_params.items():
        buffers[buffer_name] = simpy.Store(env, params["capacity"])


