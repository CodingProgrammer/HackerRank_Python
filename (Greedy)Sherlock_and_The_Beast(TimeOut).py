import sys
from itertools import product
t = int(input().strip())
for a0 in range(t):
    result = []
    n = int(input().strip())
    num_5 = [i for i in range(n + 1) if i % 3 == 0]
    num_3 = [i for i in range(n + 1) if i % 5 == 0]
    for each in product(num_5, num_3):
        if sum(each) == n:
            result.append('5' * each[0] + '3' * each[1])
    if len(result) != 0:
        print(sorted(result, key = int)[-1])
    else:
        print(-1)