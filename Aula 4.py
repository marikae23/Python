# Função que coleta informações earmazena em listas. ㅇㅁㅇ

nota = []  # Lista para armazenar notas dos alunos
nome = []  # Lista para armazenar nomes dos alunos

def lenotanome():
    try:
        quantidade_alunos = int(input("Digite a quantidade de alunos: "))
        for i in range(quantidade_alunos):
            print("Aluno {}".format(i))
            
            while True:
                try:
                    nota_aluno = float(input("Digite a nota do aluno: "))
                    if 0 <= nota_aluno <= 10:
                        break
                    else:
                        print("Nota fora do intervalo válido (0-10).")
                except ValueError:
                    print("Digite uma nota válida em número.")

            nome_aluno = input("Digite o nome do aluno: ")
            
            nota.append(nota_aluno)  # Adiciona a nota à lista 'nota'
            nome.append(nome_aluno)  # Adiciona o nome à lista 'nome'
            
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

def imprime(l):
    print(l)  # Imprime a lista
    print(id(l))  # Imprime o identificador da lista

x = [1, 6, 4, 5, 8]
imprime(x)
print(id(x))  # Imprime o identificador da lista 'x'

___________________________________________________

# Versão do professor:
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
