'''
Awesome use of bisect
'''
#!/bin/python3

import os
import sys
from bisect import bisect_right
def climbingLeaderboard(scores, alice, alice_count):
    temp_scores = sorted(set(scores))
    length = len(temp_scores)
    reverse_result = []
    for each_ele in alice:
        reverse_result.append(bisect_right(temp_scores, each_ele))
    result = [length + 1 - each for each in reverse_result]
    return '\n'.join(map(str, result))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice, alice_count)

    fptr.write(result)
    fptr.write('\n')

    fptr.close()
