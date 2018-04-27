'''
Algorithm:
Wrong: iterate the list, find S[i] and S[j] each time when (S[i] + S[j]) can NOT evenly divide k.
Why Wrong: Indeed S[i]+S[j] can NOT divide k each time, but you can not ensure that (result[j] + result[k]), in the last result, can NOT evenly divide k.

Right: 
If sum(A+B) is evenly divisible, then ((A%K)+(B%K)) is k. 
'For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by k.'
So we just need to find the remainder pairs, and choose the larger count of that pair appeared in the remainder_list.
Especially when the remainder is ZERO or is equals to k/2 when k is even, just plus one on the result.
'''
#!/bin/python3

import os
import sys
def nonDivisibleSubset(k, S):
    result = {}
    remainder_list = [each % k for each in S]
    remainder_set = set(remainder_list)
    for each_remainder in remainder_set:
        if (each_remainder in result.keys()) or ((k - each_remainder) in result.keys()):
            continue
        else: 
            if each_remainder == 0 or (k % 2 == 0 and each_remainder == k // 2):   
                result[each_remainder] = 1
            else:
                result[each_remainder] = max(remainder_list.count(each_remainder), remainder_list.count(k-each_remainder))
                
    return(sum(result.values()))
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
