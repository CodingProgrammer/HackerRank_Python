import sys
bucket = {}
if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        k, s = input().strip().split(' ')
        k, s = [str(k), str(s)]
        if a0 < n // 2:
            bucket[k] = bucket.get(k, '') + '- '
        else:
            bucket[k] = bucket.get(k, '') + s + ' '
    for k in sorted(bucket, key = int):
        print(bucket[k], end = '')
