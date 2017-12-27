'''
here k is the given length
It is guaranteed that n(len(string)) is a multiple of k. 
'''
def merge_the_tools(string, k):
    n = len(string)
    num_sub = int(n / k)
    l = []
    s_res = ''
    index = 0
    for i in range(num_sub):
        l.append(string[index : index + k])
        index += k
        for j in range(k):
            if l[i][j] in s_res:
                continue
            else:
                s_res += l[i][j]
        print(s_res)
        s_res = ''
    

s = 'AABCAAADA'
k = 3
merge_the_tools(s, k)