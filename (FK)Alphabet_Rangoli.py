import string
alpha = string.ascii_lowercase

n = int(input())
l = []
for i in range(n):
    s = '-'.join(alpha[i:n])
    l.append((s[::-1] + s[1:]).center((4 * n - 3), '-'))  #when s = 'c' , s[1:] NOT out of range?!
print('\n'.join(l[:0:-1] + l))