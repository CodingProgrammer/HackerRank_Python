'''
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left. 
Sample Input
ABCDCDC
CDC
Sample Output
2
'''
def count_substring(string, sub_string):
    if not sub_string:
        return 0
    l1 = len(string)
    l2 = len(sub_string)
    n = 0
    if l1 < l2:
        return -1
    for i in range(l1):             #travel through the original string
        j = 0                       #reset the index of the substring whenenver change a new index in original string
        k = i                       #avoid changing i(the index of the original string) unintentionally
        while k < l1 and j < l2 and string[k] == sub_string[j]: #if you want to find the first index of the sub in ori, just move 'k < l1' away
            j += 1
            k += 1
        if j == l2:
            n += 1
    return n