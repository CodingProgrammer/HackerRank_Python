'''
Make list-A reversed
Iterate A and B, add the A[i] and B[i] correspondingly and judge if tne sum is satisfied with the requirement
'''
#!/bin/python3

import sys

def twoArrays(k, A, B, n):
    for i in range(n):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        A = list(map(int, input().strip().split(' ')))
        B = list(map(int, input().strip().split(' ')))
        result = twoArrays(k, sorted(A, reverse = True), sorted(B), n)
        print(result)