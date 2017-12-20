s = input()
print(any(char.isalnum() for char in s))
print(any(char.isalpha() for char in s))
print(any(char.isdigit() for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))

'''
awesome use of any
any(iterable) return True if the iterable are not all the 0,'',False
iterable here is a list or a tuple
'''