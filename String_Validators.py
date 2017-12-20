s = input()
l_judge = [None,None,None,None,None]
for c in s:
    if c.isalnum():
        l_judge[0] = True
    if c.isalpha():
        l_judge[1] = True
    if c.isdigit():
        l_judge[2] = True
    if c.islower():
        l_judge[3] = True
    if c.isupper():
        l_judge[4] = True
for i in range(5):
    if l_judge[i] == None:
        l_judge[i] = False
    print(l_judge[i])