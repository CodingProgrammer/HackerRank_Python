#!/bin/python3

import sys

def timeConversion(s):
    hour = int(s[0:2])
    if 'P' in s :
        if hour == 12:
            return '12' + s[2:8]
        else:
            return str(hour + 12) + s[2:8]
    elif 'A' in s:
        if hour ==12:
            return '00' + s[2:8]
        else:
            return s[:8]

s = input().strip()
result = timeConversion(s)
print(result)