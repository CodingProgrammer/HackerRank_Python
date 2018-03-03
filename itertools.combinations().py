from itertools import combinations
s, k = input().split()
for i in range(1, int(k) + 1):
    for each in combinations(sorted(s), i):
        print(''.join(each))