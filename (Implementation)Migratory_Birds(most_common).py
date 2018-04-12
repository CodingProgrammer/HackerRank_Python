'''
Awesome use of most_common()
'''
#!/bin/python3

import sys

from collections import Counter
def migratoryBirds(n, ar):
    counter_birds = Counter(ar)
    return counter_birds.most_common(1)[0][0]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
