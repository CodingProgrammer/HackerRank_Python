'''
Key: Compare k and diff_pair before subtraction operation make sure string can be palindrome
'''
#!/bin/python3

import sys

def richieRich(s, n, k):
    s = list(s)
    diff_pair = len([1 for i in range(0, n // 2) if s[i] != s[n - i -1]])

    # palindrome 
    for i in range(0 , n // 2):
        if s[i] != s[n - i - 1]:
            if s[i] != '9' and s[n - i - 1] != '9':
                if k - 2 >= diff_pair - 1:
                    s[i] = s[n - i -1] = '9'
                    k -= 2
                    diff_pair -= 1
                elif k - 1 >= diff_pair - 1:
                    s[i] = s[n - i - 1] = max(s[i], s[n- i - 1])
                    k -= 1
                    diff_pair -= 1
                else:
                    return -1
            elif s[i] == '9' or s[n - i -1] == '9':
                if k - 1 >= diff_pair - 1:
                    s[i] = s[n -i - 1] = '9'
                    k -= 1
                    diff_pair -= 1
                else:
                    return -1
        else: #s[i] != s[n - i - 1]
            if s[i] != '9':
                if k - 2 >= diff_pair: #make sure after k - 2 operation, the string can still be transefed to palindrome
                    s[i] = s[n - i - 1] = '9'
                    k -= 2
    if k > 0 and n % 2 != 0:
        s[n // 2] = '9'
        k -= 1
    return (''.join(s))
n, k = map(int, (input().split()))
s = input().strip()
result = richieRich(s, n, k)
print(result)