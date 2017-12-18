N = int(input('number:'))
i = 0
command = input('command:')
l = []
res_list = []
while i  < N:
    l = command.split()
    if l[0] == 'insert':
        res_list.insert(int(l[1]), int(l[2]))
    elif l[0] == 'print':
        print(res_list)
    elif l[0] == 'remove':
        res_list.remove(int(l[1]))
    elif l[0] == 'append':
        res_list.append(int(l[1]))
    elif l[0] == 'sort':
        res_list.sort()
    elif l[0] == 'pop':
        res_list.pop()
    elif l[0] =='reverse':
        res_list.reverse()
    i += 1
    if i == N:
        break
    command = input('command:')
print(res_list)