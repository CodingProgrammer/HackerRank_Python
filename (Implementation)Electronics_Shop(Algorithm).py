'''
Algorith: We sort keyboards in descending order. We sort usb in ascending order. 
Then we iterate over them not checking usbs past where 1 usb plus our current keyboard is already greater than s.

result recoreds the value of last operation, 'keyboards[i] + drives[j] > b' can not use '='
use while loop to avoid iterating the second list from the beginning.
'''
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, n, m, b):
    keyboards.sort(reverse = True)
    drives.sort()
    result = -1
    i, j = 0, 0
    while i < n:
        while j < m:
            if keyboards[i] + drives[j] > b:
                break
            if keyboards[i] + drives[j] >= result:
                result = keyboards[i] + drives[j]
            j += 1
        i += 1
    return result

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

    moneySpent = getMoneySpent(keyboards, drives, n, m, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
