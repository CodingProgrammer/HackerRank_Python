'''
Algorithm:https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
'''
#!/bin/python3

import sys

def commonChild(s1, s2):
    # generate a 2-dimentional arrey
    mymatrix = [[None for i in range(0, len(s1)  + 2)] for j in range(0, len(s1) + 2)]
    #inialize the 2-d array
    for i in range(0, len(s1)):
        mymatrix[0][i + 2] = s1[i]
        mymatrix[i + 2][0] = s2[i]
        mymatrix[1][i + 2] = 0
        mymatrix[i + 2][1] = 0
    mymatrix[1][1] = 0
    #fill the array
    for i in range(2, len(s1) + 2):
        for j in range(2, len(s1) + 2):
            if mymatrix[i][0] != mymatrix[0][j]:
                mymatrix[i][j] = max(mymatrix[i-1][j], mymatrix[i][j-1])
            else:
                mymatrix[i][j] = mymatrix[i-1][j-1] + 1
    return mymatrix[-1][-1]

s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)
