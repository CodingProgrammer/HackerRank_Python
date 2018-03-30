'''
Compared with the TimeOut one, the first step is to sort the original list.
So the problem become to find min(arr[i+k-1] - arr[i]).
'''

#!/bin/python3

import sys
def angryChildren(k, arr, n):
    result = []
    for i in range(n - k + 1):
        result.append(arr[i + k - 1] - arr[i])
    return min(result)

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = angryChildren(k, sorted(arr), n)
    print(result)