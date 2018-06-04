def is_valid_coordinates(coordinates):
	if coordinates.count(',') > 1:
		return False
	if ',' not in coordinates:
		if coordinates.count(' ') > 0 or coordinates.count('.') > 1 or coordinates.count('-') > 1:
			return False
	for each in coordinates:
		if each.isnumeric() or each == '.' or each == '-':
			continue
		else:
			return False
		
	Latitude, Longitude = coordinates.split(',')
	if Latitude.count('-') > 1 or Longitude.count('-') > 1 or Latitude.count('.') > 1 or Longitude.count('.') > 1:
		return False
	if Latitude.count(' ') > 0 or Longitude.count(' ') > 1:
		return False
	if '-' in Latitude and Latitude.index('-') != 0:
		return False
	if '-' in Longitude:
		if ' ' in Longitude:
			if Longitude.index('-') != 1:
				return False
	else:
		if Longitude.index('-') != 0:
			return False
		
	for each in Latitude:
		if each.isnumeric() or each == '.' or each == '-':
			continue
		else:
			return False

	for each in Longitude:
		if each.isnumeric() or each == '.' or each == '-' or (each == ' ' and Longitude.index(each) == 0):
			continue
		else:
			return False

	if float(Latitude) < -90 or float(Latitude) > 90 or float(Longitude) < -180 or float(Longitude) > 180:
		return False

	return True 

  
