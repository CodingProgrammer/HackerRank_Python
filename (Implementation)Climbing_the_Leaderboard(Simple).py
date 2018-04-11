'''
To solve the TimeOut problem use rank to record the position checked last time.
When the score_alice in alice is equal to the element in socres set, skip it.
'''
#!/bin/python3

import os
import sys
def climbingLeaderboard(scores, alice, alice_count):
    scores_set = sorted(set(scores), reverse = True)
    result = []
    rank = len(scores_set)
    for each_score in alice:
        while rank > 0 and (each_score >= scores_set[rank - 1]):
            rank -= 1
        result.append(rank + 1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice, alice_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
