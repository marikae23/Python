# Função que retorna o valor da potencia >_<

import math

def pot(x, y):
    i = y 
    while i > 0:
        i = i - 1

x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))

z = pot(x, y)
print(z)

print(math.sqrt(9))

___________________________________________________

import math

while True:
    try:
        x = int(input("Digite a base: "))
        y = int(input("Digite o exponte: "))
        break

    except:
        print("Somente números")

print(pow(x, y))
print(math.sqrt(45))

___________________________________________________

import math

def pot(x, y):
    i = y 
    z = 1
    while i > 0:
        i = i - 1
        z = z * x
    return(z)

def entrada():
    try:
        x = int(input("Digite a base: "))
        y = int(input("Digite o expoente: "))

    except:
        print("Somente números")
    return(x, y)

q, p = entrada()
def imprime(w):
    print("Resultado: ", w)

z = pot(q, p)
print(z)
