import numpy as np

def RandomArray(size, interval):
    return np.random.randint(interval[0], interval[1], size)

def isSorted(data) -> bool:
    return all(a <= b for a, b in zip(data, data[1:]))

def remove(array, element):
    result = []
    for idx, i in enumerate(array):
        if i == element:
            for j in range(len(array)):
                if j != idx:
                    result.append(array[j])
            return result