#!/bin/python3

import sys
from collections import Counter
def sherlockAndAnagrams(s):
    # Complete this function
    num = 0
    for i in range(0, len(s)):
        for length in range(1, len(s)):
            pattern_string = s[i:i + length]
            for start in range(i + 1, len(s) - length + 1):
                test_string = s[start:start + length]
                s_pattern = Counter(pattern_string)
                s_test = Counter(test_string)
                if s_pattern == s_test:
                    num += 1
    return num

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
