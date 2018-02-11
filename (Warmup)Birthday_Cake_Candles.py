#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    print(ar.count(max(ar)))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
birthdayCakeCandles(n, ar)