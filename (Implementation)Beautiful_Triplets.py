#!/bin/python3

import sys

def beautifulTriplets(d, arr):
    length = len(arr)
    ans = 0
    
    for i in range(length):
        flag = 0
        for j in range(i + 1, length):
            if flag == 0:
                if arr[j] - arr[i] == d:
                    for k in range(j + 1, length):
                        if (arr[k] - arr[i]) == 2 * d:
                            ans += 1
                            flag = 1
                            break
            else:
                break
            
    return ans

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
