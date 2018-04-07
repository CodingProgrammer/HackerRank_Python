#!/bin/python3

import sys

def pickingNumbers(a):
    result = [[each] for each in set(a)]
    for each_element in a:
        for each_row in result:
            if abs(each_element - min(each_row)) <= 1:
                each_row.append(each_element)
            else:
                continue
    return max([len(each) - 1 for each in result])

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(sorted(a))
    print(result)
