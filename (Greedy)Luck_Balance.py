#!/bin/python3

import sys

def luckBalance(n, k, contests):
    sum_decrease = 0
    bucket = {'0':[], '1':[]}
    for each in contests:
        if each[1] == 0:
            bucket['0'].append(each[0])
        else:
            bucket['1'].append(each[0])
    for i in range(len(bucket['1']) - k):
        sum_decrease += min(bucket['1'])
        bucket['1'].remove(min(bucket['1']))
    
    return sum(bucket['1']) + sum(bucket['0']) - sum_decrease

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in range(n):
       contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
       contests.append(contests_t)
    result = luckBalance(n, k, contests)
    print(result)
