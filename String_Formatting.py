def print_formatted(number):
    w = len(bin(number)) - 2
    for i in range(1, number + 1):
        b = bin(i)[2:].rjust(w)
        o = oct(i)[2:].rjust(w)
        h = hex(i)[2:].upper().rjust(w)
        j = str(i).rjust(w)
        print (j, o, h, b)
'''
.format
 print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = width)
 awesome use of {}
'''
