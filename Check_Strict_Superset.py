A, n = set(map(int, input().split())), int(input())
for i in range(n):
    new_set = set(map(int, input().split()))
    if new_set < A:
        if i == n - 1:
            print(True)
        continue
    else:
        print(False)
        break