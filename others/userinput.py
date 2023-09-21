from others import global_variable

# Define a data structure to store machine parameters
global_variable.machine_params = {
    "Machine1": {
        "failure_modes": [
            {    "name" : "M1FM1",
                "failure_dist": "weibull",
                "repair_dist": "exponential",
                "failure_para": [2000, 2.0],
                "repair_para": [20],
            },
            {   "name" : "M1FM2",
                "failure_dist": "exponential",
                "repair_dist": "weibull",
                "failure_para": [1800],
                "repair_para": [250, 1],
            },
            # Add more failure modes as needed
        ],
    },
    "Machine2": {
        "failure_modes": [
            {   "name" : "M2FM1",
                "failure_dist": "weibull",
                "repair_dist": "exponential",
                "failure_para": [2000, 2],
                "repair_para": [20],
            },
            {   "name" : "M2FM2",
                "failure_dist": "exponential",
                "repair_dist": "weibull",
                "failure_para": [1800],
                "repair_para": [25, 1.6],
            },
            # Add more failure modes as needed
        ],
    },
    # Add more machines with their parameters as needed
}


# Define dispatching rules (user-defined)
global_variable.dispatch_rules = {
    "JobA": "Machine1",
    "JobB": "Machine1",}
    # Add more dispatching rules for other job types

# Create a dataframe for user input
global_variable.input_data = {
    "Job Type": ["JobA", "JobB"],
    "Total Quantity": [50, 30],
    "Frequency": [3, 5],
    "Lot Size": [5, 10],
}

# Define a data structure to store buffer parameters
global_variable.buffer_params = {
    "Buffer1": {
        "capacity": 10  # Example buffer capacity
    },
    "Buffer2": {
        "capacity": 5  # Example buffer capacity
    },
    # Add more buffers with their parameters as needed
}

job_info = {
    "Job1": {
        "operations": [
            {
                "operation_name": "Operation1",
                "machines": ["Machine1", "Machine2"],
                "setup_time": 2,
                "process_time": 8,
            },
            {
                "operation_name": "Operation2",
                "machines": ["Machine2", "Machine3"],
                "setup_time": 3,
                "process_time": 7,
            },
            # Add more operations as needed
        ],
    },
    "Job2": {
        "operations": [
            {
                "operation_name": "Operation1",
                "machines": ["Machine2", "Machine4"],
                "setup_time": 1,
                "process_time": 9,
            },
            {
                "operation_name": "Operation2",
                "machines": ["Machine3", "Machine5"],
                "setup_time": 2,
                "process_time": 7,
            },
            # Add more operations as needed
        ],
    },
    # Add more jobs as needed
}
