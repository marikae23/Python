# Um armazém trabalha com 100 mercadorias diferentes identificadas pelos números inteiros de 1 a100. O dono do armazém anota a quantidade de cada mercadoria vendida durante o mês. Ele tem uma tabela que indica para cada mercadoria o preço de venda. Escreva um programa para calcular o faturamento mensal do armazém, isto é: Faturamento = somatório das quantidades vendidas vezes os preços. Onde k é a quantidade vendida e preçok é o preço da k_ésima mercadoria.


import Aulas as plt

def ler_dados(quantidade_mercadorias):
    preços = []
    quantidades_vendidas = []
    for i in range(quantidade_mercadorias):
        preço = float(input(f"Digite o preço da mercadoria {i + 1}: "))
        quantidade = int(input(f"Digite a quantidade vendida da mercadoria {i + 1}: "))
        preços.append(preço)
        quantidades_vendidas.append(quantidade)
    return preços, quantidades_vendidas

def calcular_faturamento(preços, quantidades_vendidas):
    return sum(preço * quantidade for preço, quantidade in zip(preços, quantidades_vendidas))

def imprimir_faturamento(preços, quantidades_vendidas):
    for i, (preço, quantidade) in enumerate(zip(preços, quantidades_vendidas)):
        print(f"Mercadoria {i + 1}: Preço = {preço}, Quantidade Vendida = {quantidade}")
    faturamento = calcular_faturamento(preços, quantidades_vendidas)
    print(f"Faturamento Mensal Total = {faturamento}")

def calcular_percentuais_vendas(preços, quantidades_vendidas):
    faturamento = calcular_faturamento(preços, quantidades_vendidas)
    percentuais = [preço * quantidade / faturamento for preço, quantidade in zip(preços, quantidades_vendidas)]
    return percentuais

def gravar_dados_vendas(preços, quantidades_vendidas):
    with open("dados_vendas.txt", "w") as file:
        for preço, quantidade in zip(preços, quantidades_vendidas):
            file.write(f"Preço: {preço}, Quantidade Vendida: {quantidade}\n")

def imprimir_grafico(preços, quantidades_vendidas):
    sorted_data = sorted(enumerate(quantidades_vendidas), key=lambda x: x[1], reverse=True)
    top_5 = sorted_data[:5]
    mercadorias = [i + 1 for i, _ in top_5]
    vendas = [quantidade for _, quantidade in top_5]

    plt.bar(mercadorias, vendas)
    plt.xlabel('Mercadorias')
    plt.ylabel('Quantidade Vendida')
    plt.title('Cinco Mercadorias Mais Vendidas')
    plt.show()

def main():
    quantidade_mercadorias = int(input("Digite o número de mercadorias: "))
    preços, quantidades_vendidas = ler_dados(quantidade_mercadorias)

    while True:
        print("\nMenu:")
        print("1. Inserir preços e quantidades vendidas")
        print("2. Calcular faturamento mensal")
        print("3. Imprimir faturamento")
        print("4. Calcular percentuais de vendas por mercadoria")
        print("5. Gravar dados das vendas em arquivo")
        print("6. Imprimir gráfico das cinco mercadorias mais vendidas")
        print("7. Sair")

        opção = input("Escolha uma opção: ")

        if opção == '1':
            preços, quantidades_vendidas = ler_dados(quantidade_mercadorias)
        elif opção == '2':
            faturamento = calcular_faturamento(preços, quantidades_vendidas)
            print(f"Faturamento Mensal Total = {faturamento}")
        elif opção == '3':
            imprimir_faturamento(preços, quantidades_vendidas)
        elif opção == '4':
            percentuais = calcular_percentuais_vendas(preços, quantidades_vendidas)
            for i, percentual in enumerate(percentuais):
                print(f"Mercadoria {i + 1}: Percentual de Vendas = {percentual * 100:.2f}%")
        elif opção == '5':
            gravar_dados_vendas(preços, quantidades_vendidas)
            print("Dados das vendas foram gravados no arquivo dados_vendas.txt")
        elif opção == '6':
            imprimir_grafico(preços, quantidades_vendidas)
        elif opção == '7':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
