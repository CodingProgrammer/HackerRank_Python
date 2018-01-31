'''
Counting-sort-1 print the keys in order
Counting-sort-2 print the values related to the keys in order
'''
import sys

def countingSort(arr):
    # Complete this function
    bucket = dict.fromkeys([str(each) for each in range(0, 100)], 0)
    for key in arr:
        bucket[key] = bucket.get(key, 0) + 1
    for key in sorted(bucket, key = int):
        for i in range(bucket[key]):
            print(key, end = ' ')


if __name__ == "__main__":
    n = int(input().strip())
    arr = input().strip().split(' ')
    result = countingSort(arr)