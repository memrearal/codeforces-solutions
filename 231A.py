lines = int(input())
problems = []
for i in range(0, lines):
	petya, vasya, tonya = map(int, input().split(" "))
	problems.append([petya, vasya, tonya])
gecerli = 0
for problem in problems:
	juri = problem[0] + problem[1] + problem[2]
	if juri >= 2:
		gecerli += 1
print(gecerli)