n = int(input())
name_number = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_number}
while True:
    name_seek = input()
    if name_seek in phone_book:
        print('%s=%s'%(name_seek, phone_book[name_seek]))
    elif name_seek == 'q' or name_seek == 'Q':
        break
    else:
        print('Not found')
'''
How to creak a dict due to the input
l = [input().split() for _ in range(n)]
d = {k:v for k,v in l}
'''