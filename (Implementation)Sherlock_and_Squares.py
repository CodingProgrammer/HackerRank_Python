'''
Count all integers found between the square roots given.
'''
#!/bin/python3

import sys

import math
def squares(a, b):
    return int(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
