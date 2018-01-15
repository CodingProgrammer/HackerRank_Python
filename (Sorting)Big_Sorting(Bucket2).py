'''
Awesome use of lambda
Firstly, a given element x is compared based on it's length,followed by its regular sorted value, 
effectively performing a bucket sort as seen in the other posts.
'''
#!/bin/python3

import sys

def bigSorting(arr):
    # Complete this function
    return sorted(arr, key = lambda x : (len(x), x))

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = str(input().strip())
       arr.append(arr_t)
    result = bigSorting(arr)
    print ("\n".join(map(str, result)))