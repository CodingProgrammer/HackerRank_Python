from collections import OrderedDict
n = int(input())
result = OrderedDict()
for _ in range(n):
    key = input()
    if key in result.keys():
        result[key] += 1
    else:
        result[key] = 1
print(len(result))
for key, value in result.items():
    print(value, end = ' ')