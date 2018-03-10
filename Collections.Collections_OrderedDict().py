from collections import OrderedDict
N = int(input())
result = OrderedDict()
for _ in range(N):
    in_put = input().split()
    key, value = ' '.join(in_put[:-1]), int(in_put[-1])
    if key in result.keys():
        result[key] += value
    else:
        result[key] = value
for key, value in result.items():   
    print(key, value)