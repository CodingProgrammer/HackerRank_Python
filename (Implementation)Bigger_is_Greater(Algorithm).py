'''
Next lexicographical permutation algorithm: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
Condensed mathematical description:

1.  Find largest index i such that array[i − 1] < array[i].
    (If no such i exists, then this is already the last permutation.)

2.  Find largest index j such that j ≥ i and array[j] > array[i − 1].

3.  Swap array[j] and array[i − 1].

4.  Reverse the suffix starting at array[i].

'''
#!/bin/python3

import sys
def biggerIsGreater(w):
    l = list(w)
    i = len(l) - 2
    while l[i] >= l[i + 1]:
        i -= 1
        if i < 0:
            return 'no answer'
    j = len(l) - 1
    while l[j] <= l[i]:
        j -= 1
    l[i], l[j] = l[j], l[i]  
    result =  ''.join(l[:i + 1]) + ''.join(l[i + 1:][::-1])
    return result  
    

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        print(result)