'''
Need not to iterate all the rannge(p , q)
The potential answers are (arr[i] + arr[i+1]) // 2 (arr is sorted) and p and q.
'''
#!/bin/python3

import sys

def sherlockAndMinimax(arr, p, q, n):
    bucket = {}
    for i in range(n - 1):
        mid = (arr[i] + arr[i + 1]) // 2
        if p <= mid <= q:
            if str(mid - arr[i]) not in bucket.keys():
                bucket[str(mid - arr[i])] = [mid]
            else:
                bucket[str(mid - arr[i])].append(mid)

    temp_set_p = set()
    temp_set_q = set()
    for each_num in arr:
        temp_set_p.add(abs(each_num - p))
        temp_set_q.add(abs(each_num - q))


    temp_key_p = str(min(temp_set_p))
    temp_key_q = str(min(temp_set_q))
    if temp_key_p not in bucket.keys():
        bucket[temp_key_p] = [p]
    else:
        bucket[temp_key_p].append(p)
    if temp_key_q not in bucket.keys():
        bucket[temp_key_q] = [q]
    else:
        bucket[temp_key_q].append(q)

    for each_key in sorted(bucket, key = int,reverse = True):
        return (min(bucket[each_key]))   

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    p, q = input().strip().split(' ')
    p, q = [int(p), int(q)]
    result = sherlockAndMinimax(sorted(arr), p, q, n)
    print(result)