'''
Algorithm: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
1. Need not use a real 2-d matrix, just use two list to replace the 2-d matrix save a lot time.
2. Use if-else statement instead of max() operation to save time.
3. Use set operation to eliminate the different elements which do not exit in s1 and s2 at the same time.
'''
#!/bin/python3

import sys

def commonChild(s1, s2):
    common = set(s1) & set(s2)
    s1 = ''.join([c for c in s1 if c in common])
    s2 = ''.join([c for c in s2 if c in common])
    # generate a two lists
    previous = [0 for i in range(len(s1) + 1)]
    current = previous[::]
    #counting
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] != s1[j - 1]:
                if previous[j] > current[j - 1]:
                    current[j] = previous[j]
                else:
                    current[j] = current[j - 1] 
            else:
                current[j] = previous[j - 1] + 1
        previous = current[::]
    return current[-1]

s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)
