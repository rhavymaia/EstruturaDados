def somatoriaLista(lista, tamanho):
    if (tamanho == 0):
        return 0
    else:
        return lista[tamanho-1] + somatoriaLista(lista, tamanho -1)

lista = [1, 2, 3, 5, 30]
print(somatoriaLista(lista, len(lista)))
