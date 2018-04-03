'''
Clearly, for 0 or 1 stones, the first player has no move, so he loses.
For any of 2, 3, 4, 5, or 6 stones, the first player can make a move that leaves 0 or 1 stones for the second player, so the first player wins.
'''
#!/bin/python3

import sys

def gameOfStones(n):
    if (n % 7) in  [0, 1]:
        return 'Second'
    else:
        return 'First'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        print(result)
