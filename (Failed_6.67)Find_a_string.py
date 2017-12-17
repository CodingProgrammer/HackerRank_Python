'''
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left. 
Sample Input
ABCDCDC
CDC
Sample Output
2
'''
string = 'abcdcdc'
sub_string = 'cdc'
l_string = len(string)
l = []
index = 0
n = 0
for i in range(0, l_string):
    index = string.find(sub_string,index + 1) #index must be added 1 here, 
    l.append(index)               #or it will be looped at the previous index
set_index = set(l)                #use 'set' to eliminate the duplicated elements             
for i in set_index:               #The elements in 'set' except -1 are the index of the sub in original
    if i > 0:
        n += 1
print(n)