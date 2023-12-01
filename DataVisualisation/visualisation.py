import matplotlib.pyplot as plt
from others.global_variable import timeline_logs
for machine_name, timeline_data in timeline_logs.items():
    plt.figure()
    plt.step(timeline_data['Time'], timeline_data['Status'], where='post', label=f'{machine_name} Status')
    plt.xlabel('Time')
    plt.ylabel('Status')
    plt.title(f'Timeline of {machine_name} Status Changes')
    plt.legend()
    plt.show()