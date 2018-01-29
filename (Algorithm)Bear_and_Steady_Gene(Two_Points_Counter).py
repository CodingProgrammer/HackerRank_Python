'''
Algorithm: Two Pointers
'''
#!/bin/python3

import sys
from collections import Counter
def steadyGene(gene):
    #create gene counter which contains the characters beyond the standard limit, if the frequency of the character is lower than limit, make it zero.
    length = len(gene)
    limit = length // 4
    count_gene = dict(Counter(gene) - Counter(A = limit, C = limit, T = limit, G = limit))
    num_c2re = sum(count_gene.values())
    # no character has to be replaced
    if num_c2re == 0:
        return 0
    start, end = 0, num_c2re
    res = length
    #create the substring counter from the length of num_c2re(number of characters to be replaced)
    count_sub = dict(Counter(gene[start:end]))
    #make the sub and gene counters include all A,C,G,T characters or it will raise Error in the while loop
    if 'A' not in count_gene:
        count_gene['A'] = 0
    if 'C' not in count_gene:
        count_gene['C'] = 0
    if 'G' not in count_gene:
        count_gene['G'] = 0
    if 'T' not in count_gene:
        count_gene['T'] = 0
        
    if 'A' not in count_sub:
        count_sub['A'] = 0
    if 'C' not in count_sub:
        count_sub['C'] = 0
    if 'G' not in count_sub:
        count_sub['G'] = 0
    if 'T' not in count_sub:
        count_sub['T'] = 0
    while end < length:
        
        hasFound = True
        for k in count_sub:
            if count_sub[k] < count_gene[k]:
                hasFound = False
                break
        
        if hasFound == True:
            # required substring has found update minimum length res
            if res > end - start:
                res = end - start
            # increase start pointer to less the length of substring if possible
            count_sub[gene[start]] -= 1
            start += 1

        elif hasFound == False:
           # required substring not found yet
            count_sub[gene[end]] += 1
            end += 1
    return(res)


if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)