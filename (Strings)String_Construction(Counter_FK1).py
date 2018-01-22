'''
Algorithm: just count how many characters(frequency more than one regard it as one)
'''
#!/bin/python3

import sys
from collections import Counter
def stringConstruction(s):
    # Complete this function
    return len(Counter(s).values())

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
