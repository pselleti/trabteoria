from functools import reduce

def soma_quadrados_pares(numeros):
    # Filtra apenas os números pares
    pares = filter(lambda x: x % 2 == 0, numeros)
    
    # Eleva os números pares ao quadrado
    quadrados = map(lambda x: x ** 2, pares)
    
    # Soma os quadrados
    soma = reduce(lambda x, y: x + y, quadrados, 0)
    
    return soma

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = soma_quadrados_pares(numeros)
print("Soma dos quadrados dos números pares:", resultado)