'''
Algorithm: find the number of different characters in s2 from s1
'''
#!/bin/python3
import sys
from collections import Counter
def anagram(s):
    length = len(s)
    if length % 2 != 0:
        return -1
    s1 = Counter(s[:length // 2])
    s2 = Counter(s[length // 2:])
    diff = s1 - s2               # equals to diff = s2 - s1
    return sum(diff.values())
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)