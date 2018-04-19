'''
If k is bigger than n, you should do 'k = k % n' operation to get the real rotation.
Because when k > n, means that after n times rotation a is still the original list.
So k = k % n
'''
#!/bin/python3

import sys

def circularArrayRotation(a, m, k, n):
    k = k % n
    new_list = a[n-k:] + a[:n-k]
    for each_index in m:
        print(new_list[each_index])
    return 0

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation(a, m, k, n)
    print ("\n".join(map(str, result)))


