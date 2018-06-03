def ranks(a):
	table = {}
	for i, value in enumerate(sorted(a, reverse = True)):
		if value not in table.keys():
			table[value] = i + 1
	result = [table[each_value] for each_value in a]
	return (result)


ranks([3,3,3,3,3,5,1])
