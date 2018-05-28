#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    initial_value = 3
    end_time = initial_value * 2 - 3
    while t > end_time:
        initial_value *= 2
        end_time = initial_value * 2 - 3 

    return (initial_value - 2) * 2 + 2 - t 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
