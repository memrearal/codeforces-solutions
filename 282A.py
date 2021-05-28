n = 0
for i in range(input()):
    k = raw_input()
    if k[0] == '+' or k[1] == '+':
        n+=1
    else:
        n-=1
print n