'''
main process :set & set
'''
#!/bin/python3
import sys
from functools import reduce
def gemstones(arr):
    # Complete this function
    return len(reduce(lambda x, y: x & y, [set(each) for each in arr]))

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)