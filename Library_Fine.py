'''
When unpack input, make sure the numbers of parameters equals to the numbers of input 
Wrong: d1, d2, d3 = [1, 2]
Wrong: d1, d2 = [1, 2, 3]
Right: d1, d2 = [1, 2]
'''

d, m, y = map(int, (input().split()))
D, M, Y = map(int, (input().split()))
if y < Y:
    fine = 0
elif y == Y:
    if m < M:
        fine = 0
    elif m == M:
        if d <= D:
            fine = 0
        else:
            fine = (d - D) * 15
    else:
        fine = (m - M) * 500
else:
    fine = 10000
print(fine)