def bubbleSort(lista):
  tamanho = len(lista)
  for j in range(0, tamanho):
    print("Iteração: %s"%(j+1))
    atual = 1
    while(atual < tamanho):
      elementoAnterior = lista[atual - 1]
      elementoAtual = lista[atual]
      if (elementoAnterior > elementoAtual):
        print("Trocou: %s e %s"%(elementoAnterior, elementoAtual))
        lista[atual] = elementoAnterior
        lista[atual-1] = elementoAtual
      else:
        print("Não trocou: %s e %s"%(elementoAnterior, elementoAtual))
      
      atual = atual + 1
    
  return lista

numeros = [8, 7, 5, 6]
print(bubbleSort(numeros))
