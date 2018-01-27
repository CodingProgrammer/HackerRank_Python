'''
Use if-else statement to replace max() operator to save some time, but it is not enough!
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
                if mymatrix[i-1][j] > mymatrix[i][j-1]:
                    mymatrix[i][j] = mymatrix[i-1][j]
                else:
                    mymatrix[i][j] = mymatrix[i][j-1]
            else:
                mymatrix[i][j] = mymatrix[i-1][j-1] + 1
    return mymatrix[-1][-1]

s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)