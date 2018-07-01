import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(0, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def Netherlandflag(arr, number, L, R):
    x = L - 1
    y = R + 1
    current = L
    while current < y:
        if arr[current] < number:
            x += 1
            arr[x], arr[current] = arr[current], arr[x]
            current += 1
        elif arr[current] > number:
            y -= 1
            arr[y], arr[current] = arr[current] ,arr[y]
        else:
            current += 1
    return (x + 1, y - 1)


l = [4, 5, 6, 7 ,8, 1, 2, 3, 4, 5, 4, 4]

n = 4

Netherlandflag(l, 4, 0, len(l)-1)

print(l)
