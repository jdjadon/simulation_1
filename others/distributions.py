import random

# Define a function to generate random failure and repair times based on a given distribution
def generate_time(distribution, params):
    if distribution == "exponential":
        return random.expovariate(params[0])
    elif distribution == "normal":
        return random.normalvariate(params[0], params[1])
    elif distribution == "weibull":
        return random.weibullvariate(params[1], params[0])
    else:
        return 0  # No failure or repair if distribution not specified