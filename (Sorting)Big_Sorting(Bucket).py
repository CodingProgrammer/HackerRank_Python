'''
Awesome use of a dict, the key of the dict is the length of the input string
'''
import sys
n = int(input().strip())
res = {}
for _ in range(n):
    number = input().strip()
    length = len(number)
    if not length in res:
        res[length] = []
    res[length].append(number)
print(res)
for key in sorted(res):
    for each in sorted(res[key]):
        print(each)
