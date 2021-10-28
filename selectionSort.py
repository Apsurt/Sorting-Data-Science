def SelectionSort(array):
    for i in range(len(array)):
        l = array[i]
        r = min(array[i:])
        array[i] = r
        
    return sorted