'''
Algorithm:
1. Creat a sub_string which contais all the sub string of original strings
2. use Counter to decide whether the elements of substrings are anagram
3. use the formula : n * (n - 1) / 2 to get the solution
'''
#!/bin/python3

import sys
from collections import Counter
def sherlockAndAnagrams(s):
    # Complete this function
    res = 0
    sub_string = []
    #generate substring (one line)
    #subs = list(s) + list(itertools.chain.from_iterable([[s[j:j+i] for j in range(len(s)-i+1)] for i in range(2, len(s))]))
    for length in range(1, len(s)):
        for start in range(0, len(s) - length + 1):
            sub_string.append(''.join(sorted(s[start:start + length])))
    counter_s = Counter(sub_string)
    for each in counter_s.values():
        if each > 1:
            res += each * (each - 1) // 2
    return res

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)