from collections import Counter
X = input()
l = input()
N = input()
sum = 0
counter_l = Counter(l.split())
for i in range(int(N)):
    key, value = input().split()
    if key in counter_l.keys() and counter_l[key] > 0:
        counter_l[key] -= 1
        sum += int(value)
print(sum)