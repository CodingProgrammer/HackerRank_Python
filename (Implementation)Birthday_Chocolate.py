'''
sum operation can handle the situation when 'list index out of range'
'''
#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    times = 0
    for i in range(n):
        if sum(s[i:i+m]) == d:
            times += 1
    return times
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)