#!/bin/python3

import sys

def marcsCakewalk(calorie, n):
    calorie = sorted(calorie, reverse = True)
    rate = [pow(2, i) for i in range(n)]
    result = [each[0] * each[1] for each in zip(calorie, rate)]
    return (sum(result))


if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie, n)
    print(result)