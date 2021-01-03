import tracemalloc
import time
from .sequential import sequential
from .comprehension import comprehension
from .generators import generators


def calculate(n, m, points, method):
    tracemalloc.start()
    start = time.time()

    if method == "s":
        result = sequential(n, m, points)
    elif method == "c":
        result = comprehension(n, m, points)
    elif method == "g":
        result = generators(n, m, points)

    end = time.time()
    _, peak = tracemalloc.get_traced_memory()
    max_memory_in_MB = peak / 1024
    time_in_s = end - start
    return result, time_in_s, max_memory_in_MB



