marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

'''
exactly, we do not need list() operation here, becaue sorted() operation will return a sorted list
awesome use of set()
pay attention to the way 'for-loop' here
awesome list expression
'''
