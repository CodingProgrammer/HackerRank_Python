'''
The sequence of cuts of x and y with the same cutting costs has no influence in the final result.
So use a dict to save the key-value, here the key is the original cost and value is the delegation of 'x' or 'y'.

'''

#!/bin/python3

import sys

def boardCutting(cost_y, cost_x):
    bucket = {}
    seg_x = 1
    seg_y = 1
    result = 0
    for i in cost_x:
        if str(i) not in bucket.keys():
            bucket[str(i)] = ''
        bucket[str(i)] += 'x'
    
    for i in cost_y:
        if str(i) not in bucket.keys():
            bucket[str(i)] = ''
        bucket[str(i)] += 'y'
    for each_key in sorted(bucket, key = int, reverse = True):
        for each_c in bucket[each_key]:
            if each_c == 'x':
                seg_x += 1
                result += int(each_key) * seg_y

            elif each_c == 'y':
                seg_y += 1
                result += int(each_key) * seg_x

    
    return result % (10 ** 9 + 7)

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        m, n = input().strip().split(' ')
        m, n = [int(m), int(n)]
        cost_y = list(map(int, input().strip().split(' ')))
        cost_x = list(map(int, input().strip().split(' ')))
        result = boardCutting(cost_y, cost_x)
        print(result)
