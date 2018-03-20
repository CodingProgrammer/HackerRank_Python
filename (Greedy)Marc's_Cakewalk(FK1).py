#!/bin/python3

import sys

def marcsCakewalk(calorie, n):
    return sum([each[0] * each[1] for each in zip(sorted(calorie, reverse = True), [pow(2, i) for i in range(n)])])



if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie, n)
    print(result)