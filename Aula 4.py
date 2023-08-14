# Função

nota = []
nome = []

def lenotanome ():
    x = int(input("Digite a quantidade de alunos: "))
    for i in range(x):
        print("Aluno {}" .format(i))
        n = float(input("Digite a nota do aluno: "))
        m = input("Digite o nome do aluno: ")
        nota.append(n)
        nome.append(m)

def avalianota():
    for i in range(len(nome)):
        if nota[i] >= 9.0 and nota[i] <= 10:
            print("O alubno {} tem conceito A e nota {}" .format(nome[i], nota[i]))
        if nota[i] <= 9.0 and nota[i] >= 8.0:
            print("O aluno {} tem conceito B e nota {}" .format(nome[i], nota[i]))
        if nota[i] >= 7.0 and nota[i] <= 8.0:
            print("O aluno {} tem conceito C e nota {}" .format(nome[i], nota[i]))
        
print("O programa começa aqui")
lenotanome()
print("Meio do programa")
avalianota()
print("Fim do programa")
