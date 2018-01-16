'''
Awesome Idea: Not to split the string and judge whether it is beautiful, but to generate beautiful strings and decide whether it is 
equal to the string
The difference between this one with the Version1 is: This Version can get an early break when len(generate-sub-string) > 1/2 len(s)
'''
#!/bin/python3

import sys

def separateNumbers(s):
    if s[0] == s:
        print('NO')
        return
    for i in range(1, len(s)):
        # if the length of first-segment(i) surpass half length of s, not beautiful
        if i > len(s) / 2:
            print('NO')
            break
        mystack = []
        mystack.append(s[:i])
        while len(''.join(mystack)) < len(s):
            mystack.append(str(int(mystack[-1]) + 1))
        #Jump from while loop when the length of mystack is equal to the length of s
        #judge whether the string of mystack if equal to s 
        if ''.join(mystack) == s:
            print('YES', mystack[0])
            break
        #For now, the loop creats all the possible beautiful strings, if not find the wanted one, then 'NO'
        if i == len(s) - 1:
            print('NO')

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)