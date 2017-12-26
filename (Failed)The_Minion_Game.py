'''
1.use set() method to find Vowels and UnVowels
2.iterate the character in set() to  find the sub_string
Limitation: Only the first one index of the character in set() can be found, that means
this method will ignore other index of the character in the original string, so it is
not enough to meet the right answer.
'''
def minion_game(string):
    vowels = 'AEIOU'
    def count_substring(string, sub_string):
        len_string = len(string)
        len_sub = len(sub_string)
        n = sum([1 for i in range(len_string - len_sub + 1) if string[i:i + len_sub] == sub_string]) 
        return n
    def count_allsub(string, sub_string, index):
        step = 2
        count = 0
        while len(sub_string) <= len(string):
            if sub_string in string:
                count += count_substring(string, sub_string)
            if index != -1 and (index + step) <= len(string):
                sub_string = string[index : index + step]
                step += 1
            else:
                break
        return count 

    list_vowels = []
    for c in string:
        if c in vowels:
            list_vowels .append(c)
    set_vowels = set(list_vowels)
    count_Kevin = 0
    for c in set_vowels:
        sub_string_Kevin = c
        index_Kevin = string.find(sub_string_Kevin)
        count_Kevin += count_allsub(string, sub_string_Kevin, index_Kevin)
    list_NOTvowels = []
    for c in string:
        if (c in vowels) == False:
            list_NOTvowels.append(c)
    set_NOTvowels = set(list_NOTvowels)
    count_Stuart = 0 
    for c in  set_NOTvowels:
        sub_string_Stuart = c    
        index_Stuart = string.find(sub_string_Stuart)
        count_Stuart += count_allsub(string, sub_string_Stuart, index_Stuart)
    print(count_Kevin)
    print(count_Stuart)
    if count_Stuart > count_Kevin:
        winner = 'Stuart'
        print("{} {}".format(winner, count_Stuart))
    elif count_Stuart < count_Kevin:
        winner = 'Kevin'
        print("{} {}".format(winner, count_Kevin))
    else:
        print('Draw')
string = 'BAANANAS'
minion_game(string)


