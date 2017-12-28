"""
You can use self to define a variable not only in __init__
And the max absolute difference just equal to (max - min)
"""
class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        print(self.__elements)
        self.maximumDifference = max(self.__elements) - min(self.__elements)
    
a = [1, 2, 5]
d = Difference(a)
d.computeDifference()


print(d.maximumDifference)