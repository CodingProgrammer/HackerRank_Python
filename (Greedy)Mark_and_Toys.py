#!/bin/python3

import sys

def maximumToys(prices, k, n):
    prices = sorted(prices)
    num = 0
    sum_price = 0
    for i in range(n):
        sum_price += prices[i]
        if sum_price <= k:
            num += 1
        else:
            break
    return num

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k, n)
    print(result)
