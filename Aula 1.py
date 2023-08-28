# Criar um array de 10 elementos inteiros aleatórios entre -100 e 100. ㅎ_ㅎ

import random

array = [random.randint(-100, 100) for _ in range(10)]

# Imprimir o array completo
print("Array:", array)

# Imprimir o maior e o menor valor do array
print("Maior valor:", max(array))
print("Menor valor:", min(array))

___________________________________________________

# Versão do professor:
lista = [-5, 7, 43, 22, -20, 3, -28, 90, -160, 1, 20]
array = [-5, 7, 43, 22, -20, 3, -28, 90, -160, 1, 20]

print(max(lista))
print(min(lista))
print(max(array))
print(min(array))
