
'''
logic:
If 'x' container stores 'a' type of balls, than 'x' must trade all the 'a' 
type of balls from other container at the cost of all non 'a' type balls it has. 
Hence sum of non 'a' balls in 'x' == sum of all 'a' balls in other container. Adding 
number of 'a' type in 'x' to both side. This becomes sum of xth row = ath coloumn so 
all we have to do is to compare if the arrays containing all horizontal sums and vertical sums are same or not.
'''
#!/bin/python3

import sys

def organizingContainers(container, n):
    result_i = [sum(each) for each in container]
    result_j = []
    for i in range(n):
        sum_j = 0
        for j in range(n):
            sum_j += container[j][i]
        result_j.append(sum_j)
    return sorted(result_i) == sorted(result_j)

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container, n)
        print('Possible' if result is True else 'Impossible')
