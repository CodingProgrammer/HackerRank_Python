#!/bin/python3

import sys

def caesarCipher(s, k):
    # Complete this function
    new_s = ''
    for c in s:
        number = ord(c) + k % 26
        if c.islower():
            if number > 122:
                number -= 26
            new_s += chr(number)
        elif c.isupper():
            if number > 90:
                number -= 26
            new_s += chr(number)
        else:
            new_s += c
            
    return new_s

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
