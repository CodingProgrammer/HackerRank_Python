'''
Given the names and grades for each student in a Physics class of students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''
def f(a):
    return a[1]

l = []
students = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]
#sort the list by the value of student[][1]
#you can also use f(a) ,just make 'key = f'
students = sorted(students, key = lambda x : x[1], reverse = True) 
print(students)
min_ele = min(students, key = f)
for i in range(len(students)):
    if min_ele[1] != students[i][1]:
        l.append(students[i])
l.sort()
min_ele = min(l, key = f)
for i in range(len(l)):
    if min_ele[1] == l[i][1]:
        print(l[i][0])