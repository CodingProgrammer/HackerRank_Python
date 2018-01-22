'''
A anagram is palindrome if and only if the counts of characters have only one odd-number  
'''
#!/bin/python3

import sys
from collections import Counter
def gameOfThrones(s):
    # Complete this function
    num_odd = 0
    s1 = Counter(s)
    for each in s1.values():
        if each % 2 != 0:
            num_odd += 1
            # when num_odd > 1, not palindrome
            if num_odd > 1:
                return 'NO'
    return ('YES')
s = input().strip()
result = gameOfThrones(s)
print(result)