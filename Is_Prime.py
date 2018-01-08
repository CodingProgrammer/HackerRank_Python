'''
O(n ** 0.5)
'''
def isprime(x):
    if x == 1:
        print('Not prime')
        return
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            print('Not prime')
            return
    print('Prime')    
T = int(input())
for i in range(T):
    n = int(input())
    isprime(n)
