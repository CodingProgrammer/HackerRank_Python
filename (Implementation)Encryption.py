#!/bin/python3

import sys
s = input().strip()
rows = int(len(s) ** 0.5)
if rows < len(s) ** 0.5:
    columns = rows + 1
else:
    columns = rows
for i in range(columns):
    print(s[i::columns], end = ' ')