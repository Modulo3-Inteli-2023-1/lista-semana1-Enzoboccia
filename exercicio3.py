def soma_dos_aninhados(lista_de_listas):
    soma_total = 0
    
    for lista in lista_de_listas:
        for numero in lista:
            soma_total += numero
    
    return soma_total

# Teste da função
lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
resultado_soma = soma_dos_aninhados(lista_de_listas)
print("Lista de listas:", lista_de_listas)
print("Soma total dos elementos:", resultado_soma)
