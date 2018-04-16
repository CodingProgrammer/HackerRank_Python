#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    for i in range(0, min(len(s), len(t))):
        if s[i] != t[i]:
            break
    if (i == len(s) - 1 or i == len(t) - 1) and s[i] == t[i]  :
        number_diff = (len(s) - i - 1) + (len(t) - i - 1)
    else:
        number_diff = (len(s) - i) + (len(t) - i)
    #first condition checks whether both are even or both are odd ! because if that happens to be true then (k - diff) will always be even and string can always be build. HOW ?by appending then deleting or vice-versa.
    #second condition means delete the whole s string and append the whole t string.    
    if (number_diff <= k and number_diff % 2 == k % 2) or (len(s) + len(t) < k):
        return 'Yes' 
    return 'No'

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
