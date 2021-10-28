import numpy as np

def RandomArray(size, interval):
    return np.random.randint(interval[0], interval[1], size)

def isSorted(data) -> bool:
    return all(a <= b for a, b in zip(data, data[1:]))

def remove(array, element):
    for idx, i in enumerate(array):
        if i == element:
            None