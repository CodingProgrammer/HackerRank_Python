'''
Awesome use of sum()
When you use loop, be careful to use pop() operation, it may cause out of range
'''
K = int(input())
l = list(map(int, input().split()))
print((sum(set(l)) * K - sum(l)) // (K - 1))