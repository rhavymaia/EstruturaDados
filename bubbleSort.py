# Função implementa o algoritmo BubbleSort considerando o pior caso para ordenação.
def bubbleSort(lista):
  # Tamanho da lista. Define a quantidade de iterações.
  tamanho = len(lista)
  # Controlar a quantidade de Iterações.
  for j in range(0, tamanho):
    print("Iteração: %s"%(j+1))
    # Índice para iniciar as comparações entre os elementos.
    atual = 1
    while(atual < tamanho):
      # Valores dos Elementos: atual e anterior
      elementoAnterior = lista[atual - 1]
      elementoAtual = lista[atual]
      # Comparar se o elemento anterior é maior que o elemento atual.
      if (elementoAnterior > elementoAtual):
        print("Trocou: %s e %s"%(elementoAnterior, elementoAtual))
        # Trocar os elementos de posição caso o anterior seja maior de o atual.
        lista[atual] = elementoAnterior
        lista[atual-1] = elementoAtual
      else:
        # Não realizar troca apenas exibir uma mensagem.
        print("Não trocou: %s e %s"%(elementoAnterior, elementoAtual))
      
      # Incrementar o valor do índice.
      atual = atual + 1
   
  # Retornar a lista ordenada.
  return lista

numeros = [8, 7, 5, 6]
print(bubbleSort(numeros))
