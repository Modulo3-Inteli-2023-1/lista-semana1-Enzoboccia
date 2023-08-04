def soma_dos_aninhados(lista):
    soma = 0

    for sublist in lista:
        for num in sublist:
            soma += num

    return soma

lista = [[11, 22], [33], [44, 55, 66]]
resultado = soma_dos_aninhados(lista)
print(resultado)  # Output: 231

outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
resultado_outra_lista = soma_dos_aninhados(outra_lista)
print(resultado_outra_lista)  # Output: 34







