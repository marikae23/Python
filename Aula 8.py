# criar uma lista de inteiro e inserir n elementos
# inverter a lista de internos
# retornar o produto dos elementos da lista criada
# imprimir a lista
# criar um dicionário de n alunos com as respectivas notas
# imprimir os alunos com suas notas
# alterar a nota de um aluno do dicionário
# teclar <sair> ou <SAIR> para abandonar o programa

import os
import time


def menu():
    while True:
        os.system("cls")
        print("*****   M E N U   *****")
        print("1. criar uma lista de inteiro e inserir n elementos")
        print("2. inverter a lista de internos")
        print("3. retornar o produto dos elementos da lista criada")
        print("4. imprimir a lista")
        print("5. criar um dicionário de n alunos com as respectivas notas")
        print("6. imprimir os alunos com suas notas")
        print("7. alterar a nota de um aluno do dicionário")
        print("8. retornar uma lista dos elementos repetidos de duas listas - (obter as duas listas)")
        print("teclar <sair> ou <SAIR> para abandonar o programa")

        op = input("digite a opção: ")
        if op == 'sair' or int(op) == 0:
            break

        if int(op) == 1:
            lst = crialista()
        if int(op) == 2:
            l = lst.reverse
        if int(op) == 3:
            pass
        if int(op) == 4:
            imprimirlista(lst)


def crialista():
    l = []
    x = int(input("quantos elementos pra lista? "))
    while x > 0:
        elemento = int(input("digite o {} elemento da lista".format(x)))
        l.append(elemento)
        x = x - 1
    return(1)

def imprimirlista(Lista):
    print(Lista)
    time.sleep(5)

'''programa principal'''
menu()
