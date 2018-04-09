'''
Algotirhm:
iterate the list(transfered from string) from the last second index-i
1. Check the character from no.(i + 1) to the last one, if the char is larger than w[i], then record it and it's index in form of tuple in the temp list
2. Swap w[i] and min(temp) 
3. Sort w[i+1:]
4. Create a new string result = w[:i + 1] + w[i + 1:]
'''
#!/bin/python3
import sys
def biggerIsGreater(w):
    #transfer the string to list to do the index-swapping operation (w[i], w[j] = w[j], w[i])
    w = list(w)
    length_w = len(w)
    temp = []
    for i in range(length_w - 2, -1, -1):
        temp = [(w[j], j) for j in range(i + 1, length_w) if w[j] > w[i]]
        if len(temp) != 0:
            index = min(temp, key = lambda x: x[0])[1]
            w[i], w[index] = w[index], w[i]
            result = ''.join(w[:i + 1]) + ''.join(sorted(w[i + 1:]))
            return result       
    return 'no answer'

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        print(result)