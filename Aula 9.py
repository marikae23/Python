class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def grava(self):
        with open("cliente.txt", "a") as f:
            f.write(f"Nome: {self.nome}\n")
            f.write(f"Sobrenome: {self.sobrenome}\n")
            f.write(f"CPF: {self.cpf}\n")

    def ler():
        with open("cliente.txt", "r") as f:
            print("Leitura de cliente")
            content = f.read()
            print(content)
            
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def grava(self):
        with open("conta.txt", "a") as f:
            f.write(f"Número da Conta: {self.numero}\n")
            f.write(f"Saldo: {self.saldo}\n")
            f.write(f"Limite: {self.limite}\n")
            f.write(f"Titular: {self.titular}\n")
