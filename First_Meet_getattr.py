'''
getattr(object, name[, default]) -> value  means object.name
'''
_ = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    #receive the command and the number of the set
    command, _ = input().split()
    #receive the element in each set
    new_set = set(map(int, input().split()))
    #process
    getattr(A, command)(new_set)  

print (sum(A))
