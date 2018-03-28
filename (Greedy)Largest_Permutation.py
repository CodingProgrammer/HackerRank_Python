'''
To solve the timeout problem, use a dict to find the wanted elements to save time
But remember to change the index also when do the swap operation
'''
#!/bin/python3

import sys

def largestPermutation(n, k, arr):
    num_swap = 0
    table = {}
    for i in range(n):
        table[str(arr[i])] = i
        

    for i in range(n):
        if num_swap >= k:
            break

        if arr[i] != (n - i):
            a, b = arr[i], arr[table[str(n - i)]]
            arr[i], arr[table[str(n - i)]] = arr[table[str(n - i)]], arr[i]
            table[str(a)], table[str(b)] = table[str(b)], table[str(a)]
            num_swap += 1
    return arr



if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = largestPermutation(n, k, arr)
    print (" ".join(map(str, result)))