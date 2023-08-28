 # Função criar, acessar e manipular listas. ㅠ ㅅ ㅠ

print("Hello World !")  # Imprime a mensagem "Hello World !"

l = [1, 2, 57, 3, 9, 92]  # Cria uma lista chamada 'l' com os valores fornecidos

print(l)  # Imprime a lista completa: [1, 2, 57, 3, 9, 92]
print(l[4])  # Imprime o quinto elemento da lista (índice 4): 9
print(type(l))  # Imprime o tipo da variável 'l': <class 'list'>
print(len(l))  # Imprime o comprimento (número de elementos) da lista: 6
print(sum(l))  # Imprime a soma de todos os elementos da lista: 164
print(max(l))  # Imprime o valor máximo da lista: 92

l.append(88)  # Adiciona o valor 88 ao final da lista 'l'
print(l)  # Imprime a lista atualizada: [1, 2, 57, 3, 9, 92, 88]

# Versão do professor
print("Hello World !")

l = [1, 2, 57, 3, 9, 92]
print(l)
print(l[4])
print(type(l))
print(len(l))
print(sum(l))
print(max(l))
l.append(88)
print(l)
