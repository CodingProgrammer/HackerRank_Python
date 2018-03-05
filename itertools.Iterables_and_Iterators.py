from itertools import combinations
n = int(input())
s = ''.join([x for x in input() if x != ' '])
k = int(input())
num_contain_a = 0
num_all =0
for each in combinations(s, k):
    if 'a' in each:
        num_contain_a += 1
    num_all += 1
print(num_contain_a / num_all)