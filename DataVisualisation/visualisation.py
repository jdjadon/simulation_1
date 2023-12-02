import matplotlib.pyplot as plt
import numpy as np
from others.global_variable import timeline_logs

#to visualise machine timeline

def machine_timeline(timeline_logs):
    for machine_name, timeline_data in timeline_logs.items():
        plt.figure()
        plt.step(timeline_data['Time'], timeline_data['Status'], where='post', label=f'{machine_name} Status')
        plt.xlabel('Time')
        plt.ylabel('Status')
        plt.title(f'Timeline of {machine_name} Status Changes')
        plt.legend()
        plt.show()

# to visualis machine status report
# Extract states and values for each machine

def machine_status_graph(machine_data):
    machine_names = list(machine_data.keys())
    states = list(machine_data[machine_names[0]].keys())

    # Calculate fractions
    total_time = np.array([sum(machine_data[machine][state] for state in states) for machine in machine_names])
    fractions = np.array(
        [[machine_data[machine][state] / total_time[i] for state in states] for i, machine in enumerate(machine_names)])

    # Plotting
    fig, ax = plt.subplots()

    for i, machine in enumerate(machine_names):
        ax.barh(states, fractions[i], label=machine)

    ax.legend()
    plt.xlabel('Fraction of Time')
    plt.ylabel('States')
    plt.title('Machine States')
    plt.show()