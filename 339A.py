s = input()
sayilar = list()
for i in range(len(s)):
	if s[i] == "+":
		pass
	else:
		sayilar.append(s[i])

for k, sayi in enumerate(sorted(sayilar)):
	if(k == len(sayilar)-1):
		print(sayi, end="")
	else:
		print(sayi+"+",end="")