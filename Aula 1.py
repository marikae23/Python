# Criar um array de 10 elementos inteiros aleatórios entre -100 e 100

import random

array = [random.randint(-100, 100) for _ in range(10)]

# Imprimir o array completo
print("Array:", array)

# Imprimir o maior e o menor valor do array
print("Maior valor:", max(array))
print("Menor valor:", min(array))
