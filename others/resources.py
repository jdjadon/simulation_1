import simpy
from others.global_variable import *
from machine import machine


def add_machine(env):   
    for machine_name, params in machine_params.items():
        machine_resources[machine_name] = simpy.Resource(env, capacity=1)
    for machine_name, params in machine_params.items():
        machines[machine_name] = env.process(
            machine.machine(env, machine_name, params, machine_resources[machine_name]))
    return machine_resources, machines

def add_buffer(env):
    for buffer_name, params in buffer_params.items():
        buffers[buffer_name] = simpy.Store(env, params["capacity"])