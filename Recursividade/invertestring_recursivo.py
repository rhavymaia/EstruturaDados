def inverte(texto, indice=-1):
	if(indice == -1):
		indice = len(texto) - 1
	# caso indice seja maior que zero:
	if(indice > 0):
		# recuperar última letra e concatenar com a chamada recursiva.
		return texto[indice] + inverte(texto, indice-1)
	else:
		return texto[indice]

texto = str(input("Informe um texto:"))
textoInverso = inverte(texto)
print(textoInverso)
