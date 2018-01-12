'''
use the list expression to generate
'''
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    s = list(range(1, n + 1))
    l = [s[i]&s[j] for i in range(len(s)) if s[i] < k for j in range(i+1, len(s)) if s[i] & s[j] < k]
    print(max(l))