'''
Analyze the last failure one , I plan to iterate the original string with different steps
and judge the first character in sub_string which is sub_string[0]. 
if sub_string[0] is a vowel, Kevin get 1 point
else Stuart get 1 point
'''
def minion_game(string):
    l = len(string)
    vowels = 'AEIOU'
    count_Kevin = 0
    count_Stuart = 0
    for step in range(1, l + 1):
        for index in range(0, l - step + 1):
            sub_string = string[index : index + step]
            if sub_string[0] in vowels:
                count_Kevin += 1
            else:
                count_Stuart += 1
    if count_Stuart > count_Kevin:
        winner = 'Stuart'
        print("{} {}".format(winner, count_Stuart))
    elif count_Stuart < count_Kevin:
        winner = 'Kevin'
        print("{} {}".format(winner, count_Kevin))
    else:
        print('Draw')