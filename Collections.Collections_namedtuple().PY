'''
A new way to creat 2-dimentional matrix(especially with the tilte)
'''
from collections import namedtuple
N, spredsheet = input(), namedtuple('spredsheet', input().split())
result = (spredsheet._make(input().split()) for _ in range(int(N)))
print("{:.2f}".format(sum([int(each.MARKS) for each in result]) / int(N)))