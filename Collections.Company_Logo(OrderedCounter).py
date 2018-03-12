'''
Awesome use of OrderedCounter
'''
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
[print(*each) for each in OrderedCounter(sorted(input())).most_common(3)]