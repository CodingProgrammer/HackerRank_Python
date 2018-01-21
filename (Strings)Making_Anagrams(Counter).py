'''
Algorithm: The anagram is hidden in the (s1 & s2)
'''
#!/bin/python3
import sys
from collections import Counter
def makingAnagrams(s1, s2):
    # Complete this function
    s1_c = Counter(s1)
    s2_c = Counter(s2)
    diff_1 = s1_c - s2_c
    diff_2 = s2_c - s1_c
    return sum(diff_1.values()) + sum(diff_2.values())
s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)