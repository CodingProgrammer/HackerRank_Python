from collections import defaultdict
A = defaultdict(list)
n, m = input().split()
for i in range(int(n)):
    c = input()
    A[c].append(str(i + 1))
for j in range(int(m)):
    key = input()
    if key in A.keys():
        print(' '.join(A[key]))
    else:
        print(-1)