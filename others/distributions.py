import random

# Define a function to generate random failure and repair times based on a given distribution
def generate_time(distribution, params):
    if distribution == "exponential":
        return random.expovariate(params["lambda"])
    elif distribution == "normal":
        return random.normalvariate(params["mean"], params["std_dev"])
    elif distribution == "weibull":
        return random.weibullvariate(params["shape"], params["scale"])
    else:
        return 0  # No failure or repair if distribution not specified