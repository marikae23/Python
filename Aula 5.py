# Função que retorna o valor da potencia. ㅜㅁㅜ 

import math

def pot(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        half_pow = pot(x, y // 2)  # Calcula metade da potência
        return half_pow * half_pow  # Eleva a metade ao quadrado para obter a potência completa
    else:
        return x * pot(x, y - 1)  # Caso ímpar: multiplica x pela potência anterior

x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))

z = pot(x, y)  # Calcula a potência usando a função 'pot'
print(z)  # Imprime o resultado da potência

print(math.sqrt(9))  # Calcula a raiz quadrada de 9 usando a função da biblioteca math

___________________________________________________

# Versão do professor:
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

﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏

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

﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏

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

﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏

t = ("osmar", 123, 4, 5,[1, 2, 32, 4])
print(type(t))
print(type(t[3]))
print(l)
print(t)
print("O tamanho da tupla e", len(t))
l1 - t[3]

for i in t:
    print(i)

aluno = {
    "01" : "Pedro",
    "02" : "Antonio",
    "10" : "Isabela",

    "Lista" : [8.0, 9.0, 7.6, 8.0]
}
print(aluno.values())
print(aluno.keys())
print(aluno["01".aluno["Lista"][0]])
print(aluno['Lista'])
print(aluno["Lista"][0])

tup = (1, 3)
