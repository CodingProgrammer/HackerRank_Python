'''
Introduce the Loop Invariant conception.
Loop invariant is nothing but a condition or a logical expression that must evaluate to true as long as the loop is progressing towards achieving the desired goal
http://www.8bitavenue.com/2012/01/introduction-to-loop-invariants/
'''
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))