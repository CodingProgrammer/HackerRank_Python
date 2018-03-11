for _ in range(int(input())):
    n, l = input(), list(map(int, input().split()))
    result = 'Yes'
    if max(l) not in (l[0], l[-1]):
        result = 'No'
    print(result)