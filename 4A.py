weight = int(input(""))
if weight <= 100 and weight >= 1:
	if weight % 2 == 0 and weight>2:
		print("YES")
	else:
		print("NO")