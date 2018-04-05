'''
Awesome use of a standard pre-table model
'''
#!/bin/python3

import sys
table = [
[2, 7, 6, 9, 5, 1, 4, 3, 8],
[2, 9, 4, 7, 5, 3, 6, 1, 8],
[4, 3, 8, 9, 5, 1, 2, 7, 6],
[4, 9, 2, 3, 5, 7, 8, 1, 6],
[6, 1, 8, 7, 5, 3, 2, 9, 4],
[6, 7, 2, 1, 5, 9, 8, 3, 4],
[8, 1, 6, 3, 5, 7, 4, 9, 2],
[8, 3, 4, 1, 5, 9, 6, 7, 2]
]
def formingMagicSquare(l):
    result = []
    for each_magic in table:
        cost = 0
        for i in range(9):
            cost += abs(l[i] - each_magic[i])
        result.append(cost)
    return min(result)

if __name__ == "__main__":
    l = []
    s_t = ''
    for _ in range(3):
       s_t += input() + ' '
    l = list(map(int, s_t.split()))
    result = formingMagicSquare(l)
    print(result)
