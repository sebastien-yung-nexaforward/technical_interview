# Imports
from typing import List

def triSub(L, low, high):
    low = 0
    high = len(L) - 1
    pivot = partition(L, low, high)
    triSub(L, pivot + 1, high)
    triSub(L, low, pivot - 1)

def tri(L: List[int]):
    """
    Quick sort
    """
    pass
    

def partition(L, low, high) -> int:
    """
    Determine the index for partition
    """
    i = low - 1
    pivot = high
    while i <= pivot:
        if L[i] > L[pivot]:
            L[i], L[pivot] = L[pivot], L[i]
    L[i+1], L[pivot] = L[pivot], L[i+1]
    return i + 1


