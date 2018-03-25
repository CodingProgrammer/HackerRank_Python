#!/bin/python3

import sys
from collections import Counter
def beautifulPairs(A, B, n):
    result = 0
    count_A = Counter(A)
    count_B = Counter(B)
    for key in count_A:
        result += min(count_A[key], count_B[key])
    if result < n:
        return result + 1
    else:
        return result - 1


if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    result = beautifulPairs(A, B, n)
    print(result)