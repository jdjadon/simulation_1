from others import global_variable

# Define a data structure to store machine parameters
global_variable.machine_params = {
    "Machine1": {
        "status" : "idle",
        "Entry" : "Buffer1",
        "Exit"  : "Buffer2",
        "current_job" : 'NULL',
        "Remaining_process_time" : 0,
        "failure_modes": [
            {    "name" : "M1FM1",
                "failure_dist": "weibull",
                "repair_dist": "weibull",
                "failure_para": [3, 3000],
                "repair_para": [3, 20],
                 "ttf": 0,
                "ttr" : 0
            },
            {   "name" : "M1FM2",
                "failure_dist": "weibull",
                "repair_dist": "weibull",
                "failure_para": [3, 3000],
                "repair_para": [3, 10],
                "ttf": 0 ,
                "ttr" : 0
            },

            # Add more failure modes as needed
        ],
    },
    "Machine2": {
        "status" : "idle",
        "Entry" : "Buffer2",
        "Exit"  : "Buffer3",
        "current_job" : 'NULL',
        "Remaining_process_time" : 0,
        "failure_modes": [
            {   "name" : "M2FM1",
                "failure_dist": "weibull",
                "repair_dist": "exponential",
                "failure_para": [3, 3000],
                "repair_para": [20],
                "ttf" : 0,
                "ttr" : 0
            },
            {   "name" : "M2FM2",
                "failure_dist": "exponential",
                "repair_dist": "weibull",
                "failure_para": [1800],
                "repair_para": [3, 16],
                "ttf":0,
                "ttr" : 0
            },
            # Add more failure modes as needed
        ],
    },
    # Add more machines with their parameters as needed
}


# Define dispatching rules (user-defined)
global_variable.dispatch_rules = {
    "Job1": "Machine1",
    "Job2": "Machine1",}
    # Add more dispatching rules for other job types

# Create a dataframe for user input
global_variable.input_data = {
    "Job Type": ["Job1", "Job2"],
    "Total Quantity": [5, 5],
    "Frequency": [1, 1],
    "Lot Size": [5, 5],
    "Dispatch to" : ["Buffer1", "Buffer1"]
}

# Define a data structure to store buffer parameters
global_variable.buffer_params = {
    "Buffer1": {
        "capacity": 1000,
        "current_status" : {},
    },
    "Buffer2": {
        "capacity": 500,
        "current_status": {},
    },
    "Buffer3": {
        "capacity": 500,
        "current_status": {},
    },
    # Add more buffers with their parameters as needed
}

global_variable.job_info = {
    "Job1": {
        "operations": [
            {
                "operation_name": "Operation1",
                "machines": ["Machine1"],
                "setup_time": 1,
                "process_time": 10,
            },
            {
                "operation_name": "Operation2",
                "machines": ["Machine2", "Machine3"],
                "setup_time": 30,
                "process_time": 10,
            },
            # Add more operations as needed
        ],
    },
    "Job2": {
        "operations": [
            {
                "operation_name": "Operation1",
                "machines": ["Machine2", "Machine4"],
                "setup_time": 3,
                "process_time": 6,
            },
            {
                "operation_name": "Operation2",
                "machines": ["Machine3", "Machine5"],
                "setup_time": 30,
                "process_time": 8,
            },
            # Add more operations as needed
        ],
    },
    # Add more jobs as needed
}
