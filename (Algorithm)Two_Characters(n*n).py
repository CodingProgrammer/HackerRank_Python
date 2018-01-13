''' 
This version create n * n matrix! n = len(temp_set) that means the dimension of the matrix flucturates depends on the original string
Algorithm: https://www.hackerrank.com/challenges/two-characters/forum/comments/280681 
New skill: Two-dimensional array  
More test examples 
1.  s = a 
    result = 0 
2.  s = ezfnjymgqtjnmstbadgdsrxvntnacwljnkgchtjeaoivfcindgxipmrjuqmmcpntpotplodjhijxqpogjmzipygacfdjgmewechuebxvcbnakszzcxkozxwavzgmesrvysonomhvufezislfntgncspthcpneyminpbjildobozfirvcgdratdpmmpkujcywvtzkdytzyfejbytsobvudvutfueveevgrqnxjiwpkrvllsjxmqhotlnpgjxkjnobxfqodlyiqsisdeuwqmntxouzdtisgutdafostmwticvncjwldpknuodmfksusaqpsoosgpiveyxipfklmhypdxpdncpgaswpycoxsuxasqduojpblctcyvyxldcgzevedvxiwinfppkjbtifuuapickknwxxjmjmtxlpfalxdgepmekaxijuphqfafrnezyldokwcnzenhpibktlfuxjfmeqajmvopbhuslnnnlmkmoteceiwbytjhhxqnkuazevswrkaofggfrnapciuoexqogscugzspwuvzkyrdfkhixcaqctfwadewpqksxxvqiigvjjpagvqikuojlwhfyztu 
    result = 0 
3.  s = uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon 
    result = 0 
''' 

import sys 
def find_max(matrix): 
    new_matrix = [] 
    for i in range(1, len(matrix)): 
        new_matrix.append(max(matrix[i][1:])) 
    return max(new_matrix) 
 
def twoCharaters(s): 
    
    #d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25 } 
    temp_set = sorted(set(s))
    length = len(temp_set) 
    mymatrix = [[None for col in range(-1, length)] for row in range(-1, length)] 
    res = [[0 for col in range(-1, length)] for row in range(-1, length)] 
    #inialize res and mymatrix
    for index, c in enumerate(temp_set): 
        mymatrix[0][index + 1] = c
        mymatrix[index + 1][0] = c
        res[0][index + 1] = c
        res[index + 1][0] = c
        res[index][index] = -1
    res[length][length] = -1

    for c in s:
        c_index = mymatrix[0].index(c) 
        #row operation 
        for i in range(1, length + 1): 
            if c_index != i and mymatrix[c_index][i] == c: 
                res[c_index][i] = -1 
            mymatrix[c_index][i] = c 
            if res[c_index][i] != -1: 
                res[c_index][i] += 1 
         
        #col operation 
            if c_index != i and mymatrix[i][c_index] == c: 
                res[i][c_index] = -1 
            mymatrix[i][c_index] = c 
            if res[i][c_index] != -1: 
                res[i][c_index] += 1 
    ans = find_max(res) 
    if ans == -1: 
        return 0 
    return ans 
  
#test 
s = 'beabeefeab' 
result = twoCharaters(s) 
print(result) 