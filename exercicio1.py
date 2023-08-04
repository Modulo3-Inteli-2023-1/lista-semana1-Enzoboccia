def multiplas_operacoes(a, b):
  
    soma = a + b
    
    subtracao = a - b
    
    multiplicacao = a * b
    
    if b != 0:
        divisao = a / b
    else:
        divisao = 0
    
    return soma, subtracao, multiplicacao, divisao

resultado = multiplas_operacoes(10, 2)
print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])
print("Divisão:", resultado[3])










