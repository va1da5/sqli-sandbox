import functools
import random
from time import sleep

from app.core.config import settings


def simulate_network_latency(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not settings.SIMULATE_NETWORK_LATENCY:
            return func(*args, **kwargs)

        sleep(random.randint(50, 150) / 1000)
        output = func(*args, **kwargs)
        sleep(random.randint(50, 150) / 1000)
        return output

    return wrapper
