'''
Algorithm: Two Pointers
'''
#!/bin/python3

import sys
def steadyGene(gene):
    length = len(gene)
    limit = length // 4
    count_gene = {'A':0, 'C':0, 'G':0, 'T':0}
    for c in gene:
        count_gene[c] += 1
    for key, value in count_gene.items():
        if value > limit:
            count_gene[key] = value - limit
        else:
            count_gene[key] = 0
    num_2re = sum(count_gene.values())
    if num_2re == 0:
        return 0
    start, end = 0, 0
    res = length
    count_sub = {'A':0, 'C':0, 'G':0, 'T':0}
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
    return res


if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)
