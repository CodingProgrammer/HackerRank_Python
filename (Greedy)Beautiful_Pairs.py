#!/bin/python3

import sys
def beautifulPairs(A, B, n):
    result = 0
    bucket_A = set()
    bucket_B = set()
    for i in range(n):
        for j in range(n):
            if A[i] == B[j]:
                if i not in bucket_A and j not in bucket_B:
                    bucket_A.add(i)
                    bucket_B.add(j)
                    result += 1
                    break
    if result == n:
        return result - 1
    else:
        return result + 1

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    result = beautifulPairs(A, B, n)
    print(result)