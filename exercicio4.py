def tem_duplicados(lista):

    conjunto = set()

    for elemento in lista:
        if elemento in conjunto:
            return True
        conjunto.add(elemento)

    return False


lista1 = [1, 2, 3, 4, 5]
print(tem_duplicados(lista1)) 

lista2 = [1, 2, 3, 4, 5, 1]
print(tem_duplicados(lista2))  








