"""
Job Generator for Simulated Manufacturing System

This defines a job generator function for a simulated manufacturing system using Simpy. The job generator
creates and dispatches jobs of a specified type at regular intervals. Each job consists of a quantity of items to
be produced and is assigned to a specific machine or buffer for processing.

Purpose:
    The job generator simulates the creation of jobs in a manufacturing environment. It allows users to specify
    the type of job, the total quantity of jobs to be generated, the time interval between job generations, and
    the lot size (quantity of jobs generated in each batch).

Inputs:
    - env (simpy.Environment): Simpy environment in which the simulation is run.
    - job_type (str): Type of job to generate (e.g., "TypeA", "TypeB").
    - total_quantity (int): Total number of jobs to generate.
    - frequency (float): Time interval (in simulation time units) between job generations.
    - lot_size (int): Number of jobs to generate in each batch.

Outputs:
    This function generates jobs of the specified job_type at regular intervals and records information about each
    generated job. The job information includes the job type, quantity, the machine to which it's dispatched, and the
    time it was generated. The generated jobs are stored in the global variable 'job_record' for further analysis
    and tracking.

Example Usage:
    # Create a Simpy environment
    env = simpy.Environment()

    # Define job generation parameters
    job_type = "TypeA"
    total_quantity = 100
    frequency = 10.0  # Time interval between job generations (e.g., 10 time units)
    lot_size = 5

    # Start the job generator process
    env.process(job_generator(env, job_type, total_quantity, frequency, lot_size))

    # Run the simulation for a specified duration
    env.run(until=100)  # Run the simulation for 100 time units

Global Variables:
    The code assumes the existence of the following global variables, which are used to store and track generated jobs:
    - machine_params (dict): Dictionary of machine parameters, mapping machine names to their properties.
    - dispatch_rules (dict): Dictionary of dispatch rules, mapping job types to preferred machine names.
    - job_record (list): List of generated job dictionaries, recording job information.

Note:
    The global variables 'machine_params', 'dispatch_rules', and 'job_record' should be imported and defined
    externally in the 'others.global_variable' module or within the simulation environment for the code to work
    correctly.
"""
