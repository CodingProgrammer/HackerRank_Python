'''
Algorithm: Just make the string the max 
Failer: Can not assure the string is palindrome
'''
#!/bin/python3

import sys

def richieRich(s, n, k):
    s = list(s)
    for i in range(0, n // 2 + 1):
        
        if k == 1 and s == s[::-1]:
            s[n // 2] = '9'
            k -= 1
        
        if k <= 0:
            break

        if s[i] != s[n - i - 1]:
            if s[i] != '9' and s[n -i - 1] != '9' and k >= 2:
                s[i] = s[n- i - 1] = '9'
                k -= 2
            elif (s[i] == '9' or s[n - i - 1] == '9') and k >= 1:
                s[i] = s[n- i - 1] = '9'
                k -= 1
        elif s[i] == s[n - i - 1]:
            if s[i] != '9' and k >= 2:
                s[i] = s[n - i -1] = '9'
                k -= 2
    if s == s[::-1]:
        return ''.join(s)
    return -1
n, k = map(int, (input().split()))
s = input().strip()
result = richieRich(s, n, k)
print(result)