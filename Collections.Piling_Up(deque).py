from collections import deque
T = int(input())
for _ in range(T):
    n, l = input(), deque(map(int, input().split()))
    previous = max(l[0], l[-1])
    while len(l) > 0:
        if l[0] >= l[-1]:
            if previous < l[0]:
                break
            previous = l.popleft()
        elif l[0] < l[-1]:
            if previous < l[-1]:
                break
            previous = l.pop()
    print('Yes' if len(l) == 0 else 'No')