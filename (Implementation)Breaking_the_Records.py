#!/bin/python3

import sys

def breakingRecords(score):
    max_score, min_score = score[0], score[0]
    max_n, min_n = 0, 0
    for each in score[1:]:
        if each > max_score:
            max_score = each 
            max_n += 1
        elif each < min_score:
            min_score = each
            min_n += 1
    return max_n, min_n

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
