from bubbleSort import BubbleSort
from tools import RandomArray, isSorted
from selectionSort import SelectionSort
from bubbleSort import BubbleSort

def main():
    for i in range(1000):
        arr = RandomArray(5, (0,100))
        sorted = BubbleSort(arr)
        correct = isSorted(sorted)
        #print(correct, sorted)
        if (i+1)%100 == 0:
            print(i+1)
        if not(correct):
            break
        
main()