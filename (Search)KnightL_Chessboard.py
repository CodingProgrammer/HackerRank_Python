'''
step by step
In each step, find all the possible location(defferent set level) of the KnightL 
If the final location in the possible location(set with different level), return the current level
If the set of the possible location repeated, return -1

ToDo: BFS algorithm
'''
def step(x, y, a, b, n):
    level = 0
    l = [{(x, y)}]
    while min(x, y) + min(a, b) < n:
        level += 1
        l.append(set())
        for each in l[level - 1]:
            if 0 <= (each[0] + a) < n and 0 <= (each[1] + b) < n:
                l[level].add((each[0] + a, each[1] + b))
            if 0 <= (each[0] + a) < n and 0 <= (each[1] - b) < n:
                l[level].add((each[0] + a, each[1] - b))
            if 0 <= (each[0] - a) < n and 0 <= (each[1] + b) < n:
                l[level].add((each[0] - a, each[1] + b))
            if 0 <= (each[0] - a) < n and 0 <= (each[1] - b) < n:    
                l[level].add((each[0] - a, each[1] - b))
            if 0 <= (each[0] + b) < n and 0 <= (each[1] + a) < n:
                l[level].add((each[0] + b, each[1] + a))
            if 0 <= (each[0] + b) < n and 0 <= (each[1] - a) < n:
                l[level].add((each[0] + b, each[1] - a))
            if 0 <= (each[0] - b) < n and 0 <= (each[1] + a) < n:
                l[level].add((each[0] - b, each[1] + a))
            if 0 <= (each[0] - b) < n and 0 <= (each[1] - a) < n:
                l[level].add((each[0] - b, each[1] - a))
            
            if (n-1, n-1) in l[level]:
                return level
        if l[level] in l[: level - 1]:
            return -1

def KnightL(n):
    for i in range(1, n):
        for j in range(1, n):
            print(step(0, 0, i, j, n), end = ' ')
        print(sep = '')

n = int(input().strip())
KnightL(n)