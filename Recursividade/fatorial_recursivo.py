def fatorial(n):
    if (n == 1):
        return 1
    else:
        return n * fatorial(n-1)

print("Informe um número para calcular o fatorial: ", end ='')
numero = int(input())
print(fatorial(numero))
