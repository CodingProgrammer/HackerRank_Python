'''
use common(set) to regenerate s1, s2, eliminating the characters do not show in s1 and s2 at the same time
but it seems that does not work when the string is really long which contains all the 26 alphabets
'''
#!/bin/python3

import sys

def commonChild(s1, s2):
    common = set(s1) & set(s2)
    s1 = ''.join([c for c in s1 if c in common])
    s2 = ''.join([c for c in s2 if c in common])
    # generate a 2-dimentional arrey
    mymatrix = [[None for i in range(0, len(s1)  + 2)] for j in range(0, len(s2) + 2)]
    #inialize the 2-d array
    for i in range(0, len(s1)):
        mymatrix[0][i + 2] = s1[i]
        mymatrix[1][i + 2] = 0
        
    for i in range(0, len(s2)):
        mymatrix[i + 2][0] = s2[i]
        mymatrix[i + 2][1] = 0
    mymatrix[1][1] = 0
    #fill the array
    for i in range(2, len(s2) + 2):
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