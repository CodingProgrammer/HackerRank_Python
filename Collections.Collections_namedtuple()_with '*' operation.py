'''
 '*' passes elements of lists rather than whole list as a single entity.
'''
from collections import namedtuple
N, spredsheet = input(), namedtuple('spredsheet', input().split())
result = (spredsheet(*input().split()) for _ in range(int(N)))
print("{:.2f}".format(sum([int(each.MARKS) for each in result]) / int(N)))