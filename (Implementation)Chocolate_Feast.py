#!/bin/python3

import sys

def chocolateFeast(n, c, m):
    chocolate_eat = n // c
    wrappers = chocolate_eat 
    while (sum(divmod(wrappers, m)) >= m):
        chocolate_eat += wrappers // m
        wrappers = sum(divmod(wrappers, m))
    return(chocolate_eat + divmod(wrappers, m)[0])
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)