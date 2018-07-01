import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(0, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp
#L is the first element index
#R is the last element index
def quickSort(arr, L, R):
    if L < R:
        p = partition(arr, L, R)
        quickSort(arr, L, p[0] - 1)
        quickSort(arr, p[1] + 1, R)

def partition(arr, L, R):
    x = L - 1
    y = R
    current = L
    while current < y:
        if arr[current] < arr[R]:
            x += 1
            arr[x], arr[current] = arr[current], arr[x]
            current += 1
        elif arr[current] > arr[R]:
            y -= 1
            arr[y], arr[current] = arr[current] ,arr[y]
        else:
            current += 1
    arr[y], arr[R] = arr[R], arr[y]
    return (x + 1, y)


for i in range(100):
    l = GenerateRandomList(10, 1000)
    stand_l = sorted(l)
    quickSort(l, 0 ,len(l) - 1)
    if l != stand_l:
        print('What?')

print('Done!')
