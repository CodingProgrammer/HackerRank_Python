n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()       #awesome
    scores = list(map(float, line))     #awesome
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    aver = (sum(student_marks[query_name]) / 3)
print('%.2f' % (aver))  

'''
awesome use of *line, means mutable parameters

Another ways:
1. #sums = 0
    #for marks in  student_marks[query_name]:
    #    sums += marks

2.#marks = (student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2]) / 3
'''