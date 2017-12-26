'''
Just iterate once
if the character is vowel, the remain sub_string use this character at front are all belong to vowel-case
otherwise, the sub_strings are all belong to non-vowel-case
'''
def minion_game(string):
    vowels = 'AEIOU'
    count_K = 0
    count_S = 0
    l = len(string)
    for i in range(l):
        if string[i] in vowels:
            count_K += (l - i)
        else:
            count_S += (l - i)
    if  count_K  > count_S:
        print('Kevin', count_K, sep=' ')
    elif count_K < count_S:
        print('Stuart', count_S, sep=' ')
    else:
        print('Draw')
string = 'BAANANAS'
minion_game(string)