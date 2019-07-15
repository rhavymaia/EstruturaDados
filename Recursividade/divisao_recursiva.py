"""
Função divisaoRec(inteiro dividendo, inteiro divisor) retorna Inteiro
Inicio
   Se (dividendo < divisor)
   Então
      Função_Retorna(0)
   Senão
      Função_Retorna(divisaoRec(dividendo-divisor, divisor) + 1)
   Fim_Se
Fim
"""

def divisaoRec(dividendo, divisor):
    if (dividendo < divisor):
        return 0
    else:
        return divisaoRec(dividendo-divisor, divisor) + 1


print(divisaoRec(9, 2))
