import sys
def iskaprekarNumbers(n):
    length = len(str(n))
    n_square = str(n ** 2)
    left_length = len(n_square) - length
    if n_square[0:left_length] and n_square[left_length:] :
        return (int(n_square[0:left_length]) + int(n_square[left_length:])) == n
    elif len(n_square) == length:
        return int(n_square) == n

def kaprekarNumbers(p, q):
    # Complete this function
    return list(filter(iskaprekarNumbers, range(p, q + 1)))

if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    result = kaprekarNumbers(p, q)
    print (" ".join(map(str, result)) if result else 'INVALID RANGE')