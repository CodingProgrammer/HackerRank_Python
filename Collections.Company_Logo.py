from collections import Counter
s = input().strip()
counter_s = Counter(s)
items = sorted(counter_s.items())
sorted_items = sorted(items, key = lambda x : x[1], reverse = True)
i = 3
for each in sorted_items:
    print(each[0], end = ' ')
    print(each[1])
    i -= 1
    if i <= 0:
        break