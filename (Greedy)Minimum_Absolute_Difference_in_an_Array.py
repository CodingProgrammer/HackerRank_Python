'''
Awesome use of sorted firstly, and use zip function rather combinations function to speed the process
'''
import sys
def minimumAbsoluteDifference(n, arr):
    min_num = abs(int(arr[1]) - int(arr[0]))
    result = [abs(int(each[1]) - int(each[0])) for each in zip(arr, arr[1:])]
    return min(result)

if __name__ == "__main__":
    n = int(input()) 
    arr = sorted(input().split(), key = int)
    result = minimumAbsoluteDifference(n, arr)
    print(result)