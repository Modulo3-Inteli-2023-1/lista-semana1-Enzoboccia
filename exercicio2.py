def cumulativo(lista):
    cumulativa = []
    soma = 0
    
    for num in lista:
        soma += num
        cumulativa.append(soma)
    
    return cumulativa

# Teste da função
numeros = [1, 2, 3, 4, 5]
resultado_cumulativo = cumulativo(numeros)
print("Lista original:", numeros)
print("Soma cumulativa:", resultado_cumulativo)
