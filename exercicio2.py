def cumulativo(lista):
    cumulativo_list = []
    soma = 0

    for num in lista:
        soma += num
        cumulativo_list.append(soma)

    return cumulativo_list
    
lista = [2, 3, 4, 5]
resultado = cumulativo(lista)
print(resultado)  # Output: [2, 5, 9, 14]









