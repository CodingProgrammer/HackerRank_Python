n = int(input("input nums of number:"))
arr = map(int, input('input numbers:').split())
arr = list(arr)# map generate a object of map,so must use list()
max_num = max(arr)
while max_num in arr:
    arr.remove(max_num)
sec_max_num = max(arr)
print(sec_max_num)
