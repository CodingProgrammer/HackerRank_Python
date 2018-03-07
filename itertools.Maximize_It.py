'''
awesome use of '*' operator
because we couldn't know the counts of the input list, so when we use the 
product operation we use '*' to wrap the input list
'''
from itertools import product
K, M = input().split()
l = []
res = set()
for _ in range(int(K)):
    l.append(map(int, input().split()[1:]))
for each in product(*l):
    res.add(sum(list(map(lambda x : x * x, each))) % int(M))
print(max(res))