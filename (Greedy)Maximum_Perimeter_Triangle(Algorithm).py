'''
use sort to solve the following problems.
f there are several valid triangles having the maximum perimeter:

    1.Choose the one with the longest maximum side (i.e., the largest value for the longest side of any valid triangle having the maximum perimeter).
    2.If more than one such triangle meets the first criterion, choose the one with the longest minimum side (i.e., the largest value for the shortest side of any valid triangle having the maximum perimeter).
    3.If more than one such triangle meets the second criterion, print any one of the qualifying triangles.

'''
n = int(input())
sides = sorted(map(int, input().split()))
i = n - 3
while i >= 0 and ((sides[i] + sides[i + 1]) <= sides[i + 2]):
    i -= 1
if i >= 0:
    print(sides[i], sides[i+1], sides[i+2])
else:
    print(-1)