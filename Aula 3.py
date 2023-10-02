# Tipos de lista ^ㅁ^

l = [5, 4, 3, 2, 8, 7, 4, 9]  # Criação da lista 'l'

# Imprime o número de elementos na lista
print(len(i))

# Imprime os 3 últimos elementos da lista
print(i[5:])  # Isso imprimirá [7, 4, 9]

# Ordena a lista em ordem crescente
i.sort()
print(i)  # A lista agora será [2, 3, 4, 4, 5, 7, 8, 9]

# Ordena a lista em ordem decrescente
i.sort(reverse=True)
print(i)  # A lista agora será [9, 8, 7, 5, 4, 4, 3, 2]

# Insere o elemento 11 no início da lista
i.insert(0, 11)
print(i)  # A lista agora será [11, 9, 8, 7, 5, 4, 4, 3, 2]

___________________________________________________

# Versão do professor:
i = [5,4,3,2,8,7,4,9] #int
# pede-se
#1) imprima os 3 últimos elementos
#2) ordene a em ordem crescente e decrescente
#3) insira um elemento no início da l

print(len(i))
print(i[5: ]) # se eu quisesse imprimir os 3 primeiros seria print(l[ :3])
i.sort()
print(i)
i.sort(reverse=True) # ou l.reverse()
print(i)
i.insert(0, 11)
print(i)
