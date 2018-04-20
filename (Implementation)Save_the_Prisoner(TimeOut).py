'''
iterate the prisoners' list while m--
'''
#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    current_index = s
    end_index = n - 1
    while m > 0:
        if current_index > end_index:
            current_index = 0
        m -= 1
        current_index += 1
    return current_index

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m - 1, s)
    print(result)
