'''
Iterate the string and remove s[i] each time to creat a new sub_string, after that judge whether the new string is Palindrome
'''
#!/bin/python3
import sys
def palindromeIndex(s):
    # Complete this function
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        new_s = s[0:i] + s[i+1:]    #remove a character
        if new_s == new_s[::-1]:    #judge Palindrome
            return i

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)