# Função

nota = []
nome = []

def lenotanome ():
    try:
        quantidade_alunos = int(input("Digite a quantidade de alunos: "))
        for i in range(quantidade_alunos):
            print("Aluno {}".format(i))
            
            while True:
                try:
                    nota = float(input("Digite a nota do aluno: "))
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("Nota fora do intervalo válido (0-10).")
                except ValueError:
                    print("Digite uma nota válida em número.")

            nome = input("Digite o nome do aluno: ")
            
            notas.append(nota)
            nome.append(nome)
            
    except ValueError:
        print("Digite uma quantidade válida de alunos.")

def avalianota():
    for i in range(len(nome)):
        if 9.0 <= nota[i] <= 10:
            conceito = "A"
        elif 8.0 <= nota[i] < 9.0:
            conceito = "B"
        elif 7.0 <= nota[i] < 8.0:
            conceito = "C"
        else:
            conceito = "D"

    print("O aluno {} tem conceito {} e nota {}".format(nome[i], conceito, nota[i]))
        
print("O programa começa aqui")
lenotanome()
print("Meio do programa")
avalianota()
print("Fim do programa")

___________________________________________________

def imprime(l):
    print(l):
    print(id(l)):

x = [1, 6, 4, 5, 8]
imprime(x)
print(id(x))
