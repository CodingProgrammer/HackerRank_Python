import sys
from collections import Counter
def missingNumbers(arr, brr):
    l = []
    Counter_A = Counter(arr)
    Counter_B = Counter(brr)
    for key in sorted(Counter_A):
        if Counter_A[key] != Counter_B[key]:
            l.append(key)
    return l

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))