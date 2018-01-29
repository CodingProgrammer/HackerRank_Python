'''
Algorithm:
1. If the window between start and end indices contains all the characters which repeat more than n//4 times, then we find the proable solution. So increse the start pointer to see whether the new substring is still dissatisfied.
2. If the window does not contain all the required characters, increase the end pionter 
Failer: Maybe the Counter() operation wasted a lot of time, try creat yourown dictionarty to counting.
'''
#!/bin/python3

import sys
from collections import Counter
def steadyGene(gene):
    # Complete this function
    length = len(gene)
    res = length
    counetr_gene = Counter(gene)
    standard = len(gene) // 4
    counter_stan = Counter(A = standard, C = standard, T = standard, G = standard)
    counter_2re = counetr_gene - counter_stan
    num_2re = sum(counter_2re.values())
    if num_2re == 0:
        return 0
    start, end = 0, num_2re
    while end < length:
        if Counter(gene[start:end]) & counter_2re == counter_2re:
            while start < end and Counter(gene[start + 1:end]) & counter_2re == counter_2re:
                start += 1
            if res > (end - start):
                res = end - start
        end += 1
    return (res)

if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)