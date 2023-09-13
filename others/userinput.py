# Define a data structure to store machine parameters
machine_params = {
    "Machine1": {
        "failure_dist": "weibull",
        "repair_dist": "exponential",
        "maintenance_dist": "normal",
        "shape": 1.0,
        "scale": 10.0
    },
    "Machine2": {
        "failure_dist": "exponential",
        "repair_dist": "weibull",
        "maintenance_dist": "normal",
        "shape": 1.0,
        "scale": 10.0
    },
    # Add more machines with their parameters as needed
}