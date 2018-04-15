#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards = sorted([each_keyboards for each_keyboards in keyboards if each_keyboards < b], reverse = True)
    drives = sorted([each_drives for each_drives in drives if each_drives < b], reverse = True)
    result = set()
    for each_keyboards in keyboards:
        for each_drives in drives:
            if each_keyboards + each_drives <= b:
                result.add(each_keyboards + each_drives) 
    if len(result) != 0:
        return max(result)            
    return (-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
