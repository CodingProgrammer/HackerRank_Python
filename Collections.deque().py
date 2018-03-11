from collections import deque
result = deque()
N = int(input())
for _ in range(N):
    in_put = input().split()
    if in_put[0] == 'append':
        result.append(in_put[1])
    elif in_put[0] == 'pop':
        result.pop()
    elif in_put[0] == 'popleft':
        result.popleft()
    elif in_put[0] == 'appendleft':
        result.appendleft(in_put[1])
print(' '.join(result))