def print_rangoli(size):
    import string
    s = string.ascii_lowercase
    l = []
    for c in s:
        l.append(c)            # or l = list(s) can produce ['a', 'b'....],too
    for i in range(size):
        print('-'.join(l[size - 1 : size - i - 1 : -1] + l[size - 1 - i : size]).center((size - 1) * 4 + 1,'-'))
    for i in range(size - 2, -1, -1):
        print('-'.join(l[size - 1 : size - i - 1 : -1] + l[size - 1 - i : size]).center((size - 1) * 4 + 1,'-'))