def char_detector(strings):
	for i in strings:
		if i == "+":
			return i
			break
		elif i == "-":
			return i
			break
				

def plus(math):
	db_math = []
	try:
		sp = math.split("-")
		db_math.extend(sp)
		d = sum(map(int, db_math))
		print(d)
	except ValueError as ve:
		print(ve)


plus("20-20")

# if mystr("e+"):
# 	print("checked")
# else:
# 	print("no checked")
# "abcdefghijklmnopqrstuvwxyz":


