'''
In my own version, TimeOut
In this version, awesome use of 'key = int'
'''
import sys

def bigSorting(arr):
    # Complete this function
    arr = sorted(arr, key = int)
    return arr

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = str(input().strip())
       arr.append(arr_t)
    result = bigSorting(arr)
    print ("\n".join(map(str, result)))
