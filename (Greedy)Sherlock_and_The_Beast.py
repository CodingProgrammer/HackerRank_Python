'''
Wanted the biggest number, so the more 5's the bigger the integer
so reverse the order of the list of numbers of 5, and the first number meet the requirement 
is the desired one
'''
import sys
from itertools import product
t = int(input().strip())
for a0 in range(t):
    
    result = []
    n = int(input().strip())
    
    num_5 = [i for i in range(n + 1) if i % 3 == 0][::-1]
    num_3 = [i for i in range(n + 1) if i % 5 == 0]
    for each in product(num_5, num_3):
        if sum(each) == n:
             result.append('5' * each[0] + '3' * each[1])
             break
    if len(result) != 0:
        print(sorted(result, key = int)[-1])
    else:
        print(-1)
    