if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()     #arr.sort() and then arr changed
    n = arr[-1]    #you can also use arr = sorted(arr)
    while n in arr: 
        arr.pop()
    sec_max_num = max(arr)
    print(sec_max_num)