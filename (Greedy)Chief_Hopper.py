#!/bin/python3

import sys
from itertools import count
def chiefHopper(arr):
    
    for botEnergy in count(1):
        temp = botEnergy
        for each_height in arr:
            if each_height > botEnergy:
                botEnergy -= (each_height - botEnergy)
            else:
                botEnergy += (botEnergy - each_height)
            if botEnergy < 0:
                break

        if botEnergy >= 0:
            return temp


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = chiefHopper(arr)
    print(result)
