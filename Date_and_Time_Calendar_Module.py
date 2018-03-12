import calendar
Table = {'0':'MONDAY', '1':'TUESDAY', '2':'WEDNESDAY', '3':'THURSDAY', '4':'FRIDAY', '5':'SATURDAY' , '6':'SUNDAY'}
month, day, year = input().split()
print (Table[str(calendar.weekday(int(year), int(month), int(day)))].upper())