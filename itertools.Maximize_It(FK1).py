from itertools import product
K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
result = list(map(lambda x : sum(i * i for i in x) % M , product(*N)))