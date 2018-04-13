'''
Generate a visual book like this(not sorted yet):
{'3': (6,), '2': (4, 5), '1': (2, 3), '0': (1,)} 
where the key is the step need to turn and the values are the pages in each turn
'''
#!/bin/python3

import os
import sys
def pageCount(n, p):
    #when n is even
    if n % 2 == 0:
        total_turn = n // 2
    else:
        total_turn = (n - 1) // 2
    book = {'0':(1,)}
    step = 1
    for i in range(2, n + 1, 2):
        if i + 1 > n:
            book[str(step)] = (i, )
        else:
            book[str(step)] = (i, i + 1)
        step += 1
    for i in book:
        if p in book[i]:
            turn = int(i)
            break
    return min(turn, total_turn - turn)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()