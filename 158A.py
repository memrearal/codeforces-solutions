n,k = map(int, input().split(" "))
items = input().split(" ")
dondur = 0
for i in items:
	if k<=n and int(i) > 0:
		if int(i) >= int(items[k-1]):
			dondur += 1
print(dondur)