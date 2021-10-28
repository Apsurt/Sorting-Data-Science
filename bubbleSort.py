from tools import isSorted

def BubbleSort(array):
    while not(isSorted(array)):
        for i in range(1, len(array)):
            l = array[i-1]
            r = array[i]
            if l > r:
                array[i] = l
                array[i-1] = r
    return array