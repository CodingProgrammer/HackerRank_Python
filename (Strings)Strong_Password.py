#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    ans = 0
    num_number, num_low, num_upper, num_special = 0, 0, 0, 0
    for each_char in password:
        if each_char in numbers:
            num_number += 1
        elif each_char in lower_case:
            num_low += 1
        elif each_char in upper_case:
            num_upper += 1
        elif each_char in special_characters:
            num_special += 1
    
    if  num_number < 1:
        ans += 1
    if num_low < 1:
        ans += 1
    if num_upper < 1:
        ans += 1
    if num_special < 1:
        ans += 1
    
    if ans + n < 6:
        return ans + (6 - ans - n)
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
