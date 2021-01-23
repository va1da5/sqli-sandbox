import functools
from flask import current_app
import random
from time import sleep

def simulate_network_latency(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not current_app.config.get("SIMULATE_NETWORK_LATENCY"):
            return func(*args, **kwargs)

        sleep(random.randint(50, 150) / 1000)
        output = func(*args, **kwargs)
        sleep(random.randint(50, 150) / 1000)
        return output
    
    return wrapper