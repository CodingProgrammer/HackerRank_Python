
'''
Use slice. 
If G[i][j:j+c] matchs P[0]: 
1.  Append the P[0] into the result list; 
2.  Iterate (r - 1) times, append G[i+k][j:j+c] into the result list, here k is in the range(1, r - 1); 
3.  Judge whether result is equal to P, if it is True, return 'YES', else clear the result (result = []) and continue.
'''
#!/bin/python3
def gridSearch(G, P, R, C, r, c):
    for i in range(R - r + 1):
        result = []
        for j in range(C - c + 1):
            if G[i][j:j+c] == P[0]:
                result.append(P[0])
                for k in range(1, r):
                    result.append(G[i+k][j:j+c])
                if result == P:
                    return 'YES'
                else:
                    result = []
                    continue
    return 'NO'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r, c = input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)
        result = gridSearch(G, P, R, C, r, c)
        print(result)
