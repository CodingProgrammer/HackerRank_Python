cube = lambda x: x ** 3

def fibonacci(n):
    result = []
    i = 0
    a, b = 0, 1
    while i < n:
        result.append(a)
        a, b = b, a + b
        i += 1
    return result

print(list(map(cube, fibonacci(int(input())))))