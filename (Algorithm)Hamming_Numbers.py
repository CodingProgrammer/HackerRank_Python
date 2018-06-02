def hamming(n):
	result = [1]
	i, j, k = 0, 0, 0
	
	for _ in range(1, n):
		p1 = 2 * result[i]
		p2 = 3 * result[j]
		p3 = 5 * result[k]
		result.append(min(p1, p2, p3))
		if result[-1] == p1:
			i += 1
		if result[-1] == p2:
			j += 1
		if result[-1] == p3:
			k += 1
	print(result[-1])

hamming(5000)
