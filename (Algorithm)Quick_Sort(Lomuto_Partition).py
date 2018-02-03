'''
Algorithm:The algorithm maintains index i as it scans the array using another index j such that the elements lo through i (inclusive) are less than or equal to the pivot, and the elements i+1 through j-1 (inclusive) are greater than the pivot. 
It is less efficient than Hoare's original scheme
reference: https://en.wikipedia.org/wiki/Quicksort
'''
import time

def quicksort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quicksort(A, low, p - 1 )
        quicksort(A, p + 1, high)

def partition(A, low, high):
    pivot = A[high]
    # i is the lastest index whose value is lower than the pivot
    # so if the value of j-index is lower than pivot again, swap (A[i + 1], A[j])
    i = low - 1    
    for j in range(low, high):
        if A[j] < pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]  
    if A[high] < A[i + 1]:
        A[i + 1], A[high] = A[high], A[i + 1] 
    return i + 1


l = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
start = time.clock()
quicksort(l, 0 , len(l) - 1)
end = time.clock()
print(l)
print('Time: %s seconds' %(end -start))