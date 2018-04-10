'''
Solution to TimeOut:
go from the lowest to highest and start at index that you checked last time 
that way you wont need to go through entire array every time!
'''
#!/bin/python3

import os
import sys

def climbingLeaderboard(scores, alice, alice_count):
    temp_scores = sorted(set(scores), reverse = True)
    result = []
    ans = ''
    index_original = len(temp_scores) - 1
    index_alice = 0
    while index_original >= 0 and index_alice <= alice_count - 1:
        if alice[index_alice] < temp_scores[index_original]:
            result.append(index_original + 2)
            index_alice += 1

        elif alice[index_alice] > temp_scores[index_original]:
            if alice[index_alice] > temp_scores[index_original - 1]:
                index_original -= 1
            elif alice[index_alice] < temp_scores[index_original - 1]:
                result.append(index_original + 1)
                index_alice += 1
            else:
                index_original -= 1
                result.append(index_original + 1)
                index_alice += 1

        else:
            result.append(index_original + 1)
            index_original -= 1
            index_alice += 1
            
    pre = [1 for _ in range(alice_count - len(result))]
    if len(result) != 0:
        ans = '\n'.join(map(str, result)) + '\n'
    if len(pre) != 0:
        ans += '\n'.join(map(str, pre))
    return ans

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
