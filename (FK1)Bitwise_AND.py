'''
To find the maximum and less than K, so K - 1 is the first criminal we can thought
when K is odd, K - 1 is even, K - 1 can always be reached by (K - 1) & K and now ((K - 1) | K) <= n is always True as ((K - 1) | K) == K
when K is even, K - 1 is odd, K - 1 can only be reached if and only if ((K - 1) | K) <= n, so when ((K - 1) | K) > n, we choose K - 2 as our second criminal
'''
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    print(k - 1 if(k | k - 1) <= n else k - 2)