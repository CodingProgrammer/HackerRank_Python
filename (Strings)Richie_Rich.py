'''
Algorithm:https://www.hackerrank.com/challenges/richie-rich/forum
The comparison between k and diff_pair before change string make sure the string can be transfered to a palindrome
'''
#!/bin/python3

import sys

def richieRich(s, n, k):
    s = list(s)
    diff_pair = len([1 for i in range(0, n // 2) if s[i] != s[n - i -1]])

    # palindrome 
    for i in range(0, n // 2):
        if s[i] == s[n - i -1] and s[i] != '9' and k - 2 >= diff_pair:
            s[i] = s[n - i -1] = '9'
            k -= 2

        elif s[i] != s[n -i - 1] and (s[i] == '9' or s[n - i -1] == '9'):
            if k - 1 >= diff_pair - 1:
                s[i] = s[n - i - 1] = '9'
                k -= 1
                diff_pair -= 1
            else:
                return -1
        elif s[i] != s[n - i -1] and(s[i] != '9' and s[n - i - 1] != '9'):
            if k - 2 >= diff_pair - 1:
                s[i] = s[n - i - 1] = '9'
                k -= 2
                diff_pair -= 1
            elif k - 1 >= diff_pair - 1:
                s[i] = s[n - i - 1] = max(s[i], s[n - i - 1])
                k -= 1
                diff_pair -= 1
            else:
                return -1 
    if k > 0 and n % 2 != 0:
        s[n // 2] = '9'
        k -= 1
    return (''.join(s))
n, k = map(int, (input().split()))
s = input().strip()
result = richieRich(s, n, k)
print(result)