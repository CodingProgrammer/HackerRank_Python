'''
Awesome use of generater and any()
step 1 : creat a list containing different character-sets
step 2 : creat the res list use generater 
step 3 : use any() to find the result
'''
import sys

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
s = input().strip()
n = int(input().strip())
mystack = []
level = 0
res = []
for i, c in enumerate(s):
    if i == 0:
        mystack.append([])
        mystack[level].append(c)
    elif c != s[i - 1]:
        level += 1
        mystack.append([])
        mystack[level].append(c)
    else:
        mystack[level].append(c)
for i in range(len(mystack)):
    res.append(range(d[mystack[i][0]], len(mystack[i]) * d[mystack[i][0]] + 1, d[mystack[i][0]]))

for a0 in range(n):
    x = int(input().strip())
    if any(x in each for each in res):
        print('Yes')
    else:
        print('No')