'''
Algorithm: 
1. If the string is palindrome already, max it
2. If the string is not palindrome, palindrome it and then max it
Failer: when  make a string palindrome, decrease k uncorrectly
'''
#!/bin/python3

import sys

def richieRich(s, n, k):
    # first judge whether can make s a palindrome
    num_pair_diff = 0
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            num_pair_diff += 1
    if k < num_pair_diff:
        return -1
    s = list(s)
    #is palindrome
    if s == s[::-1]:
        #max it 
        if k % 2 == 0 and k > 0:                 # k is even
            for i in range(0, n // 2 + 1):
                if k <= 0:
                    break
                while s[i] == '9':
                    i += 1
                s[i] = s[n- i - 1] = '9'
                k -= 2
        elif k % 2 != 0 and k > 0:                # k is odd
            for i in range(0, n // 2 + 1):
                if k <= 0:
                    break
                if k == 1:
                    s[n // 2] = '9'
                    k -= 1
                else:
                    while s[i] == '9':
                        i += 1
                    s[i] = s[n - i - 1] = '9'
                    k -= 2     
    #make it palindrome and max it
    else: 
        #make it palindrome
        for i in range(0, n // 2 + 1):
            if k <= 0:
                break
            if s[i] != s[n - i - 1]:
                # k - 2 operation
                if k > num_pair_diff:
                    s[i] = s[n- i - 1] = '9'
                    k -= 2
                # k - 1 operation
                elif num_pair_diff >= k > 0 :
                    s[i] = s[n - i - 1] = max(s[i], s[n - i - 1])
                    k -= 1
        #max the palindromed list
        num_to_max = len([1 for each in s if each != '9'])
        for i, char in enumerate(s):
            if k == 1:
                s[n // 2] = '9'
                k -= 1
            if k <= 0:
                break
            if char != '9':
                s[i] = s[n - i - 1] = '9'
                k -= 2

    return ''.join(s)

n, k = map(int, (input().split()))
s = input().strip()
result = richieRich(s, n, k)
print(result)