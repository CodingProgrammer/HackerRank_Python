#!/bin/python3

import sys

def jimOrders(orders, n):
    bucket = {}
    for i in range(n):
        key = str(sum(orders[i]))
        if key not in bucket.keys():
            bucket[key] = []
        bucket[key].append(i + 1)
    result = [each for j in sorted(bucket.keys(), key = int) for each in bucket[j]]
    return result

if __name__ == "__main__":
    n = int(input().strip())
    orders = []
    for orders_i in range(n):
       orders_t = [int(orders_temp) for orders_temp in input().strip().split(' ')]
       orders.append(orders_t)
    result = jimOrders(orders, n)
    print (" ".join(map(str, result)))


