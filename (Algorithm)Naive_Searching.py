'''
Return the first index of pattern string in target string, if not found, return -1
Time complexity: O(m * n)
'''
def naive_searching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1

a = 'aa'
b = 'bbbbaabb'
print(naive_searching(b, a))