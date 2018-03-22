'''
#is triangle
#is maximum Perimeter
    #aera maximum
        #max maximum_side 
            #min maximum_side 
'''
#!/bin/python3

import sys
from itertools import combinations

def isTriangle(sides):
    if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
        return True
    else:
        return False
def maximumPerimeterTriangle(l):
    triangles = filter(isTriangle, set(combinations(l, 3)))
    result = {}
    for each in triangles:
        keys = str(sum(each))
        if keys not in result.keys():
            result[keys] = []
            result[keys].append(each)
        else:
            result[keys].append(each)
    if len(result) == 0:
        return [-1]
    max_maxside = max(max(each) for each in result[max(result.keys(), key = int)])
    has_maxside = [each for each in result[max(result.keys(), key = int)] if max_maxside in each]
    if len(has_maxside) == 1:
        return sorted(has_maxside[0])
    else:
        max_minside = max(min(each) for each in has_maxside)
        has_minside = [each for each in has_maxside if max_minside in each]
        if len(has_minside) != 0:
            return sorted(has_minside)
        else:
            return [-1]


if __name__ == "__main__":
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    result = maximumPerimeterTriangle(l)
    print (" ".join(map(str, result)))
