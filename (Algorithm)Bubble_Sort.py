def Bubble_Sort1(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

#if there is no swap in last iteration, that means the list is sorted.
def Bubble_Sort2(arr):
    #flag records the swap. True means there is at least one swap in last iteration, False means no swap.
    flag = True
    for i in range(len(arr)):
        if flag == False:
            break
        flag = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = True
    return arr


l = [6, 2,4, 1, 5, 9]
print(Bubble_Sort2(l))
