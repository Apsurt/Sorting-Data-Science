

def MergeSort(array):
    if len(array) > 1:
        l = array[:len(array)//2]
        r = array[len(array)//2:]

        MergeSort(l)
        MergeSort(r)
        print("L:", l)
        print("R:,", r)
    
arr = [1,23,54,2,1,324,1,54,76,96]
print(MergeSort(arr))