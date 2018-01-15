#quick-search
def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] > key:
            high -= 1
        while low < high and array[low] < key:
            low += 1
        array[low], array[high] = array[high], array[low]
    #array[low] = key
    return low

def Quick_Search(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        Quick_Search(array, low, key_index)
        Quick_Search(array, key_index + 1, high)
    #return array

l = [2, 1, 3, 5, 4]
Quick_Search(l, 0, len(l) - 1)
print(l)