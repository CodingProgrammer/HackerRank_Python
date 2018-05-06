#!/bin/python3

import os
import sys
def taumBday(b, w, bc, wc, z):
    #
    # Write your code here.
    #
    ans = 0
    if bc > wc + z:
        return (wc * (b + w) + z * b)
    
    if wc > bc + z:
        return (bc * (b + w) + z * w)
    
    return (b * bc + w * wc)

b, w = 10, 10

bc = 1

wc = 1

z = 1

result = taumBday(b, w, bc, wc, z)
print(result)

