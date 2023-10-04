import numpy as np

def generate_random_variable(distribution, *params):
    if distribution == 'normal':
        mean, std_dev = params
        return np.random.normal(mean, std_dev)
    elif distribution == 'uniform':
        low, high = params
        return np.random.uniform(low, high)
    elif distribution == 'exponential':
        scale = params[0]
        return np.random.exponential(scale)
    elif distribution == 'weibull':
        shape, scale = params
        return np.random.weibull(shape) * scale
    else:
        raise ValueError("Unsupported distribution: " + distribution)


