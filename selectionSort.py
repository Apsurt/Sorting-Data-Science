from tools import remove

def SelectionSort(array):
    sorted = []
    for _ in range(len(array)):
        r = min(array)
        sorted.append(r)
        array = remove(array, r)
    return sorted