class cliente:
    def __init__(self,cpf,nome):
        self.cpf = cpf
        self.nome = nome

class historico:
    def __init__(self):
        self.mov = []

    def movimento(self,mov):
        self.mov.append(mov)

    def imprimir(self):
        print("Historico: ")
        for x in self.mov:
            print(x)



class conta:
    def __init__(self,cliente,saldo_ini=0):
        self.cliente = cliente
        self.saldo = saldo_ini
        self.historico = historico()
   

    def deposit(self,valor):
        self.saldo += valor
        self.historico.movimento(f"deposito {valor}")

    def sacar(self,valor):
        if valor < self.saldo:
            self.saldo -= valor
            self.historico.movimento(f"saque {valor}")
        else:
            print("saldo insuficiente")

    def transferencia(self,conta_2,valor):
        if valor<self.saldo:
            self.sacar(valor)
            conta_2.deposit(valor)
            self.historico.movimento(f"Transferência para {conta_2.cliente.nome}: {valor}")
            conta_2.historico.movimento(f"Transferência de {self.cliente.nome}: {valor}")
        else:
            print("saldo insuficiente")

def achar_conta(cpf,contas):
    for x in contas:
        if x.cliente.cpf == cpf:
            return x
        else:
            pass
    return None


def main():
    clientes = []
    contas = []
    while True:
        print("Menu: \n1:Criar conta\n2:saque\n3:deposito\n4:transferencia\n5:imprimir cliente/conta/historico\n0:sair")
        escolha = int(input("digite opcao:"))
        if escolha == 0:
            break
        elif escolha == 1:
            print("\n")
            cpf = input("cpf:")
            nome = input("nome:")
            novo = cliente(cpf,nome)
            clientes.append(novo)

            saldo = int(input("saldo:"))
            novo_conta = conta(novo,saldo)
            contas.append(novo_conta)
            print("\n")

        elif escolha==2:
            print("\n")
            cpf = input("digite o cpf:")
            conta_escolhida = achar_conta(cpf,contas)
            if conta_escolhida:
                valor = int(input("valor para saque:"))
                conta_escolhida.sacar(valor)
                print("\n")
            else:
                print("conta nao encontrada")
                print("\n")


        elif escolha==3:
            print("\n")
            cpf = input("digite o cpf:")
            conta_escolhida = achar_conta(cpf,contas)
            if conta_escolhida:
                valor = int(input("valor para deposito:"))
                conta_escolhida.deposit(valor)
                print("\n")
            else:
                print("conta nao encontrada")
                print("\n")

        elif escolha==4:
            print("\n")
            cpf = input("digite o cpf da primeira conta:")
            conta_escolhida = achar_conta(cpf,contas)
            cpf = input("digite o cpf da segunda conta:")
            segunda_conta = achar_conta(cpf,contas)
            if conta_escolhida:
                valor = int(input("valor para transferencia:"))
                conta_escolhida.transferencia(conta_escolhida,segunda_conta,valor)
                print("\n")
            else:
                print("conta nao encontrada")
                print("\n")

        elif escolha==5:
            print("\n")
            cpf = input("digite o cpf:")
            conta_escolhida = achar_conta(cpf,contas)
            print(f"\nNome do usuário: {conta_escolhida.cliente.nome}, CPF: {conta_escolhida.cliente.cpf}\nSaldo atual: {conta_escolhida.saldo}")
            conta_escolhida.historico.imprimir()
            print("\n")

main()