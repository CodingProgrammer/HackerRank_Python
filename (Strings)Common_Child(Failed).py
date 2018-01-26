'''
Failer:The generated key is substring(consecutive), but the wanted are common string(not consecutive)
'''
#!/bin/python3

import sys

def commonChild(s1, s2):
    # Complete this function
    common = set(s1) & set(s2)
    #create new_s1, new_s2 
    new_s1 = ''.join([c for c in list(s1) if c in common])
    new_s2 = ''.join([c for c in list(s2) if c in common])
    #creat all the substring of new_s1
    my_dict = {}
    for length in range(1, len(new_s1) + 1):
        for start in range(0, len(new_s1) - length + 1):
            key = new_s1[start:start+length]
            my_dict[key] = my_dict.get(key, 0) + 1
    res = [len(key) for key in my_dict if key in new_s2]
    return 0 if len(res) == 0 else (max(res))

s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)
