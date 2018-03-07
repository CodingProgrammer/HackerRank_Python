import math
BC = int(input())
AB = int(input())
AC = math.hypot(AB, BC)
MBC = math.degrees(math.acos(AB / AC))
print(round(MBC),'°', sep = '')