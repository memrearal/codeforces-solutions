lines = int(input())
words = []
for i in range(0, lines):
	word = input()
	words.append(word)
for word in words:
	if len(word) > 10:
		print(word[0]+str(len(word[1::1])-1)+word[-1])
	else:
		print(word)