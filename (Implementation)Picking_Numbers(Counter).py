#!/bin/python3
import sys
from collections import Counter
def pickingNumbers(a):
    count = Counter(a)
    keys = sorted(count.keys(), key = int)
    result = []
    for i in range(len(keys) - 1):
        #line 10 and line 13: in case [1,1,1,1]
        result.append(count[keys[i]])
        if (keys[i + 1] - keys[i]) == 1:
            result.append(count[keys[i]] + count[keys[i + 1]])
    result.append(count[keys[-1]])
    return max(result)

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(sorted(a))
    print(result)
