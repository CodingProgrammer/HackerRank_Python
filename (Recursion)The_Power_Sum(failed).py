'''
TimeOut
'''
import sys
from itertools import combinations
from math import sqrt
def powerSum(X, N):
    result = []
    ans = 0
    for i in range(1, int(sqrt(X)) + 1):
        if pow(i, 2) <= X:
            result.append((pow(i, N)))
    for j in range(len(result)):
        temp = list(combinations(result, j))
        for each in temp:
            if sum(each) == X:
                ans += 1
                #print(each)
    return ans

if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)