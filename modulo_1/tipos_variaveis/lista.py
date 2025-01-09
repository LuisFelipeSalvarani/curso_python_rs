# Declaração
minha_lista = [1, 36, 3, 4, 10, 235, 5, 0]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo elementos da lista
# minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Métodos de lista

# append(): adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# index: retorna o índice de um elemento
indice = minha_lista.index(6)
print("Índice do elemetno 6:", indice)

# insert: insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# pop: remove o elemento de um índice específico
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após o pop(3):", minha_lista)

# remove: remove o primeiro elemento especificado
minha_lista.remove(True)
print("Após o remove(True):", minha_lista)

# sort: organiza a lista em ordem crescente
minha_lista.sort()
print("Após o sort():", minha_lista)
