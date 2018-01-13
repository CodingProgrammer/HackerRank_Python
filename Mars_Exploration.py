'''
Pay attention to the situation when the characters are all 'S' or 'O', but in a wrong sequence just like the test example
'''
import sys

def marsExploration(s):
    # Complete this function
    num = 0
    length = len(s)
    n = length // 3
    start = 0
    end = start + 3
    for i in range(n):
        if end > length:
            break
        sub_string = s[start:end]
        if sub_string[0] != 'S':
            num += 1
        if sub_string[1] != 'O':
            num += 1
        if sub_string[2] != 'S':
            num += 1
        start, end = end, end + 3
    return num
s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'
result = marsExploration(s)
print(result)