M,N = map(int, input().split(" "))
matriks = [[0 for x in range(M)] for y in range(N)]
top = 0
for i in matriks:
	top += len(i)
kalan = top
i = 1
while kalan >= 2:
	kalan -= 2
	i += 1
print(i-1)