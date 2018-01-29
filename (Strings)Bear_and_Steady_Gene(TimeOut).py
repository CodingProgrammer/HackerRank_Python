'''
Algorithm: Find the substring which containing the substring which is going to be replaced
'''

#!/bin/python3
import sys
from collections import Counter
def steadyGene(gene):
    # Complete this function
    counetr_gene = Counter(gene)
    standard = len(gene) // 4
    #standard string which contains (n // 4) times A, C, T and G
    counter_stan = Counter(A = standard, C = standard, T = standard, G = standard)
    #characters to be replaced
    counter_2re = counetr_gene - counter_stan
    #numbers of characters to be replaced
    num_2re = sum(counter_2re.values())
    if num_2re == 0:
        return 0
    #the length of the string to be replaced must beyond the num_2re
    for length in range(num_2re, len(gene)):
        for start in range(0, len(gene) - length + 1):
            counetr_sub = Counter(gene[start:start+length])
            if counetr_sub & counter_2re == counter_2re:
                #the first found length is the minimum length
                return sum(counetr_sub.values())

if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)