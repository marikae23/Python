class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def grava(c):
        f = open("cliente.txt", "a")
        f.write(c.nome)
        f.write(c.sobrenome)
        f.write(c.cpf)
        f.close()

    def ler(c):
        f = open("cliente.txt", "r")
        print("Leitura de cliente")
        l = f.read()
        print(l)
        #for i n f:
        #    print(i.)

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 

    def grava(c):
        f = open("conta.txt", "a")
        #cm = c.numero+str(c.saldo)+str(c.limite)+str(c.titular)
        #f.write(cn)
        f.write(c.numero)
        f.write(str(c.saldo))
        f.write(str(c.limite))
        f.write(str(c.titular))
        f.close()

while True:
    print ('''
        1. Digite os dados
        2. Ler arquivo e imprimir
        3. Sair do programa
        ''')

    op = int(input("Digite a opção: "))
    if op == 3:
        break
    if op == 1:
        n = input("Digite nome do cliente: ")
        s = input("Digite o sobrenome do cliente: ")
        c = input("Digite o CPF do cliente: ")
        num = input("Digite o número da conta: ")
        sld = input("Digitw o saldo da conta: ")
        lmy = input("Digite o limite da conta: ")
