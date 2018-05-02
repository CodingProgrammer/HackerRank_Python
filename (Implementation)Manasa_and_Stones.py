#!/bin/python3

import sys

def stones(n, a, b):
    result = set()
    i = 0
    while i < n:
        num_a = n - 1 - i
        num_b = n - 1 - num_a
        result.add(num_a * a + num_b * b)
        i += 1
    return sorted(result)

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print (" ".join(map(str, result)))


