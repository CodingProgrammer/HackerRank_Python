'''
Iteration: If c in s1 but not in s2, plus num; if c in both s1 and s2, remove c from s2
'''
#!/bin/python3

import sys

def anagram(s):
    length = len(s)
    if length % 2 != 0:
        return -1
    s1 = sorted(s[:length // 2])
    s2 = sorted(s[length // 2:])
    num = 0
    for i in range(len(s1)):
        if s1[i] not in s2:
            num += 1
        else:
            if len(s2) != 0:
                s2.remove(s1[i])
    return num
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)