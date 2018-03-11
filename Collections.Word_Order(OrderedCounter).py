'''
Awesome creating OrderedCounter-class
'''
from collections import OrderedDict, Counter
class OrderedCounter(Counter, OrderedDict):
    pass
result = OrderedCounter(input() for _ in range(int(input())))
print(len(result))
print(*result.values())