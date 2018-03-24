'''
If the number(say 66317) is not divisible by 3, it will leave a modulo of either 0,1 or 2. If I decrease the number by 5, I am basically making it a multiple of 3, and the remaning digits will be a multiple of 5 as I am subtracting it from the number.

modulo 0 implies number divisibile modulo 1 implies 5 needs to be subtracted twice. modulo 2 implies 5 needs to be subtracted once.
'''

t =int(input())
for _ in range(t):
    n = int(input())
    temp = n
    while n % 3 != 0:
        n -= 5
    if n < 0:
        print(-1)
    else:
        print(('5' * n) + ('3' * (temp - n)))