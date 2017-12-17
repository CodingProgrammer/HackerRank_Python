'''
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left. 
Sample Input
ABCDCDC
CDC
Sample Output
2
'''
so = 'abcdcdcdc'
sb = 'cdc'
l_so = len(so)
l = []
index = 0
n = 0
for i in range(0, l_so):
    index = so.find(sb,index + 1) #index must be added 1 here, 
    l.append(index)               #or it will be loop at the previous index
print(l)
set_index = set(l)                #use 'set' to eliminate the duplicated elements
print(set_index)                  #The elements in 'set' except -1 are the index of the sub in original
for i in set_index:
    if i > 0:
        n += 1
print(n)