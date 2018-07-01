import random
import copy
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(0, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp


def SmallSum(arr):
	if arr == None or len(arr) < 2:
		return 0
	return sortProcess(arr, 0, len(arr) - 1)

def sortProcess(arr, l, r):
	if l == r:
		return 0
	mid = l + (r - l) // 2
	
	return sortProcess(arr, l, mid) + sortProcess(arr, mid + 1, r) + merge(arr, l, mid, r)

def merge(arr, l, mid, r):
	temp = []
	p1 = l
	p2 = mid + 1
	res = 0
	while p1 <= mid and p2 <= r:
		if arr[p1] <= arr[p2]:
			temp.append(arr[p1])
			res += (r - p2 + 1) * arr[p1]
			p1 += 1
		else:
			temp.append(arr[p2])
			p2 += 1
	
	while p1 <= mid:
		temp.append(arr[p1])
		p1 += 1
	while p2 <= r:
		temp.append(arr[p2])
		p2 += 1
	for i in range(len(temp)):
		arr[l+i] = temp[i] 
	return res


def standard_fun(arr):
	ans = 0
	for i in range(1, len(arr)):
		for j in range(0, i):
			if arr[j] <= arr[i]:
				ans += arr[j]
	return ans

for i in range(100):
	l = GenerateRandomList(100,100)
	temp = copy.copy(l)
	standard_l = standard_fun(l)
	res = SmallSum(l)
	if res != standard_l:
		print(temp)
print('Done!')


