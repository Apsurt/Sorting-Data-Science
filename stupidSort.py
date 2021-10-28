import random as rd
from tools import isSorted

def StupidSort(array):
    shuffled = array
    while not(isSorted(shuffled)):
        rd.shuffle(shuffled)
    return shuffled