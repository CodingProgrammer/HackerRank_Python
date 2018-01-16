'''
Awesome use of itertools, especially count() func
Exactly, when start is given, the beautiful string is dertermined, so judge the remians depending on the start
'''

import sys

from itertools import count
def check_remains(start, remains):
    #A generator depending on start, judge the each element in the generated sequence 
    for each in count(start + 1):
        #To the end of the remains if not return False, then return True
        if not remains:
            return True
        if not remains.startswith(str(each)):
            return False
        #update remains
        remains = remains[len(str(each)):]

def separateNumbers(s):
    for first_length in range(1, len(s) // 2 + 1):
        start = s[:first_length]
        remains = s[first_length:]
        if check_remains(int(start), remains):
            print('YES', start)
            return
    print('NO')

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)