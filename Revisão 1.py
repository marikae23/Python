#  criar uma lista de inteiro e inserir n elementos
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
            lst = invert(lst)
        if int(op) == 3:
            print(produto_lista(lst))

        if int(op) == 4:
            imprimirlista(lst)
        if int(op) == 5:
            dic = criaDic()
        if int(op) == 6:
            imprimirDic(dic)
        if int(op) == 7:
            alterar(dic)
        if int(op) == 8:
            print(comp(lst))


def crialista():
    l = []
    x = int(input("quantos elementos pra lista?: "))
    for i in range(x):
        elemento = int(input("digite o {} elemento da lista: ".format(i+1)))
        l.append(elemento)
    return l


def imprimirlista(lista):
    print(lista)
    time.sleep(5)

def criaDic():
    dic={}
    x = int(input("elementos dicionario: "))
    for i in range(x):
        nome = input("nome:")
        nota = float(input("digite nota: "))
        dic.get(nome)
        dic[nome] = nota
    return dic

def imprimirDic(dic):
    print(dic)
    time.sleep(4)
# programa principal

def invert(lista):
    lista_invert = []
    for i in range(len(lista), 0 , -1 ):
        lista_invert.append(i)
    return lista_invert

def produto_lista(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0] * produto_lista(lst[1:])
def alterar(dic):
    x = input("digite o nome do aluno: ")
    dic[x] = int(input("digite a nova nota dele: "))

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
