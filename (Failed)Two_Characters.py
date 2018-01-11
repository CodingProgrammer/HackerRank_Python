'''
Finished function:
1.transfer 'beabeefeab' to 'babfab' p28-p44 (find the consecutive characters, and remove them all!!! from the string)
2.if the remained string's set contain 3 distinct characters, then can get the right answer
3.if the remained string's set has more than 3 distinct characers, failed!
'''
#!/bin/python3

import sys
def is_consecutive(s):
    mystack = []
    for c in s:
        if mystack:
            if c == mystack[-1]:
                return True
            else:
                mystack.append(c)
        else:
            mystack.append(c)
    return False
def delete_char(s, char):
    res = []
    for c in s:
        if c != char: 
            res.append(c)
    return res

def twoCharaters(s):
    # Complete this function
    if len(s) == 0 or len(s) == 1:
        return 0
    flag = []
    mystack = []
    len_list = []
    for c in s:
        if mystack:
            if c == mystack[-1]:
                flag.append(c)
                mystack.pop()
            else:
                mystack.append(c)
        else:
            mystack.append(c)
    for each in flag:
        while each in mystack:
            mystack.remove(each)
    temp_set = set(mystack)
    if len(temp_set) == 2:
        return len(mystack)
    temp_mystack = mystack[:]
    for c in temp_set:
        while c in temp_mystack:
            temp_mystack.remove(c)
        if len(set(temp_mystack)) > 2:
            continue
        if not is_consecutive(temp_mystack):
            len_list.append(len(temp_mystack))
        temp_mystack = mystack[:]
    if len_list:
        return max(len_list)
    
    return 0
if __name__ == "__main__":
    #l = int(input().strip())
    s = 'beabheefeab'
    result = twoCharaters(s)
    print(result)


'''
uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon
'''
