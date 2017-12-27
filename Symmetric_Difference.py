'''
use ^ to find symmetric difference
'''
M = input()
a = set(map(int, input().split(' ')))
N = input()
b = set(map(int, input().split(' ')))
ans = sorted(a ^ b)
for i in ans:
    print (i)