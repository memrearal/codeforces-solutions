matrix = list()
x,y = 0,0
iks = 0
for i in range(5):
	apList = []
	items = input().split()
	for item in items:
		if item == "1":
			x,y = iks, items.index("1")
		apList.append(item)
	matrix.append(apList)
	iks += 1

print(abs(2-x) + abs(2-y))