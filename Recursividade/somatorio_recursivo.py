def soma(x):
	if(x==1):
		return 1
	else:
		return x + soma(x-1)

print("Digina n>0")
n=int(input())
print("Soma ate ", n, "=",soma(n))
