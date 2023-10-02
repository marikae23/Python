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
    resultado = 1
    for i in range(y):
        resultado *= x
    return resultado

x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))

z = pot(x, y)
print(f"{x} elevado a {y} é igual a {z}")

raiz_quadrada = math.sqrt(9)
print(f"A raiz quadrada de 9 é igual a {raiz_quadrada}")


﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏

import math

while True:
    try:
        x = int(input("Digite a base: "))
        y = int(input("Digite o expoente: "))
        break
    except ValueError:
        print("Somente números são permitidos")

resultado_potencia = pow(x, y)
print(f"{x} elevado a {y} é igual a {resultado_potencia}")

raiz_quadrada = math.sqrt(45)
print(f"A raiz quadrada de 45 é igual a {raiz_quadrada}")

﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏

import math

def potencia(x, y):
    resultado = 1
    for _ in range(y):
        resultado *= x
    return resultado

def entrada():
    while True:
        try:
            x = int(input("Digite a base: "))
            y = int(input("Digite o expoente: "))
            return x, y
        except ValueError:
            print("Somente números inteiros são permitidos")

base, expoente = entrada()
resultado_potencia = potencia(base, expoente)

imprime(resultado_potencia)

﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏

t = ("osmar", 123, 4, 5, [1, 2, 32, 4])
print(type(t))
print(type(t[3]))

l1 = t[4]  
print(l1)
print(t)
print("O tamanho da tupla é", len(t))

for i in t:
    print(i)

aluno = {
    "01": "Pedro",
    "02": "Antonio",
    "10": "Isabela",
    "Lista": [8.0, 9.0, 7.6, 8.0]
}
print(aluno.values())
print(aluno.keys())
print(aluno["01"], aluno["Lista"][0]) 
print(aluno['Lista'])
print(aluno["Lista"][0])

tup = (1, 3)
