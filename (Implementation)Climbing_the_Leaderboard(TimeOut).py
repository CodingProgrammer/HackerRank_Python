#!/bin/python3

import os
import sys

def climbingLeaderboard(scores, alice):
    temp_scores = sorted(set(scores), reverse = True)
    result = []
    for each_score in alice:
        for i in range(len(temp_scores)):
            if each_score >= temp_scores[i]:
                result.append(i + 1)
                break
        else:
            result.append(i + 2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
