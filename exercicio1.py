def multiplas_operacoes(a, b):
    # Realiza as operações
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    
    if b != 0:
        divisao = a / b
    else:
        divisao = 0
    
    # Retorna as operações em uma tupla
    return soma, subtracao, multiplicacao, divisao

# Teste da função
valor1 = 10
valor2 = 2

resultados = multiplas_operacoes(valor1, valor2)
print("Soma:", resultados[0])
print("Subtração:", resultados[1])
print("Multiplicação:", resultados[2])
print("Divisão:", resultados[3])
