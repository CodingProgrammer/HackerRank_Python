'''
l = [i for i in range(len_string - len_sub + 1) if string[i:i + len_sub] == sub_string]
1.If you want to find the first index of the substring in the original string
l[0] is your destination

2.If you want to find every index of the snstring in the original
l[::] is what you want

3.If you want the number of times that the substring occurs in the given string
len(l) is what you want
'''
def count_substring(string, sub_string):
    len_string = len(string)
    len_sub = len(sub_string)
    n = sum([1 for i in range(len_string - len_sub + 1) if string[i:i + len_sub] == sub_string]) 
    return n


def count_substring(string, sub_string): #use recursion and a built in function
    if string.find(sub_string) < 0:
        return 0
    else:
        return 1 + count_substring(string[string.find(sub_string) + 1:], sub_string)


def hackerrankInString(s):
    # This function decide whether the substring in string(sub_string is Not secutive in the original string)
    # All the characters in substring in string(the same order also), but interrupted by some noises
    #Example: sub_string:hackerrank   string:hereiamstackerrank
    sub_string = 'hackerrank'
    length = len(sub_string)
    index = 0
    for c in s:
        if c == sub_string[index]:
            index += 1
            if index == length:
                return 'YES'
    return 'NO'