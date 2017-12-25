def capitalize(string):
    l = []
    for c in string.split(' '):   
        l.append(c.capitalize())
    return ' '.join(l)

'''
Pay attention to split(' ')
if you do not use ' ', the func will remove all the white space such as '',' ', '\n' and '\t' 
And that will change the sequence of the original string
'''