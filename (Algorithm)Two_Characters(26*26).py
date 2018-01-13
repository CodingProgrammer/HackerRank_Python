'''
This version create 26 * 26 matrix!
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
    for i in range(len(matrix)):
        new_matrix.append(max(matrix[i]))
    return max(new_matrix)

def twoCharaters(s):
    if len(s) == 1:
        return 0
    d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25 }
    #temp_set = set(s)
    length = 26
    mymatrix = [[0 for col in range(length)] for row in range(length)]
    res = [[0 for col in range(length)] for row in range(length)]
    #inialize res
    for i in range(length):
        for j in range(length):
            if i == j:
                res[i][j] = -1
    for c in s:
        #row operation
        for i in range(length):
            if d[c] != i and mymatrix[d[c]][i] == c:
                res[d[c]][i] = -1
            mymatrix[d[c]][i] = c
            if res[d[c]][i] != -1:
                res[d[c]][i] += 1
        
        #col operation
            if d[c] != i and mymatrix[i][d[c]] == c:
                res[i][d[c]] = -1
            mymatrix[i][d[c]] = c
            if res[i][d[c]] != -1:
                res[i][d[c]] += 1
    ans = find_max(res)
    if ans == -1:
        return 0
    return ans
 
#test
s = 'beabeefeab'
result = twoCharaters(s)
print(result)

