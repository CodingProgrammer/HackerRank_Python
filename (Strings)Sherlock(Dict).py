'''
Algorithm: 
1. Use the sorted substring as the key of a dict, and update the value by key
2. Formula: n * (n - 1) // 2
'''
#!/bin/python3

import sys
from collections import Counter
def sherlockAndAnagrams(s):
    # Complete this function
    my_dict = {}
    res = 0
    for length in range(1, len(s)):
        for start in range(0, len(s) - length + 1):
            subs = ''.join(sorted(s[start:start+length]))
            my_dict[subs] = my_dict.get(subs, 0) + 1
    for key in my_dict:
        if my_dict[key] > 1:
            res += my_dict[key] * (my_dict[key] - 1) // 2
    return res

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)