#Revisão

import os
import time


def menu():
    lst = []  # Inicializar a lista aqui
    dic = {}  # Inicializar o dicionário aqui

    while True:
        os.system("cls")
        print("*****   M E N U   *****")
        print("1. criar uma lista de inteiros e inserir n elementos")
        print("2. inverter a lista de inteiros")
        print("3. retornar o produto dos elementos da lista criada")
        print("4. imprimir a lista")
        print("5. criar um dicionário de n alunos com as respectivas notas")
        print("6. imprimir os alunos com suas notas")
        print("7. alterar a nota de um aluno do dicionário")
        print("8. retornar uma lista dos elementos repetidos de duas listas - (obter as duas listas)")
        print("teclar <sair> ou <SAIR> para abandonar o programa")

        op = input("digite a opção: ")

        if op.lower() == 'sair':
            break

        if op == '1':
            lst = crialista()
        elif op == '2':
            lst = invert(lst)
        elif op == '3':
            print(produto_lista(lst))
        elif op == '4':
            imprimirlista(lst)
        elif op == '5':
            dic = criaDic()
        elif op == '6':
            imprimirDic(dic)
        elif op == '7':
            alterar(dic)
        elif op == '8':
            print(comp(lst))
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)


def crialista():
    l = []
    x = int(input("quantos elementos pra lista?: "))
    for i in range(x):
        elemento = int(input("digite o {} elemento da lista: ".format(i + 1)))
        l.append(elemento)
    return l


def imprimirlista(lista):
    print(lista)
    time.sleep(5)


def criaDic():
    dic = {}
    x = int(input("quantos elementos para o dicionário?: "))
    for i in range(x):
        nome = input("nome:")
        nota = float(input("digite nota: "))
        dic[nome] = nota
    return dic


def imprimirDic(dic):
    print(dic)
    time.sleep(4)


def invert(lista):
    lista_invert = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invert.append(lista[i])
    return lista_invert


def produto_lista(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0] * produto_lista(lst[1:])


def alterar(dic):
    nome = input("digite o nome do aluno: ")
    if nome in dic:
        dic[nome] = float(input("digite a nova nota dele: "))
    else:
        print("Aluno não encontrado.")


def comp(lst):
    iguais = []
    lis = []
    y = int(input("quantos elementos pra segunda lista?: "))
    for i in range(y):
        elemento = int(input("digite o {} elemento da lista: ".format(i + 1)))
        lis.append(elemento)

    for elemento_1 in lst:
        for elemento_2 in lis:
            if elemento_1 == elemento_2:
                iguais.append(elemento_1)
    return iguais


menu()

