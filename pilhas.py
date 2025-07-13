class Pilha:
    def __init__(self):
        self.items = [] # inicializa uma pilha vazia

    def push(self, item):
        self.items.append(item) # adiciona um item ao topo da pilha

    def pop(self):
        return self.items.pop() # remove e retorna o último item da pilha

    def peek(self):
        return self.items[-1]# retorna o último item da pilha sem removê-lo

    def isEmpty(self):
        return self.items == []# verifica se a pilha está vazia

    def size(self):
        return len(self.items)# retorna o número de itens na pilha
    def ordenar(self):
        self.items.sort() # ordena a pilha em ordem crescente
    def ordenar_e_criar_nova(self):
        return sorted(self.items) 

# Exemplo de uso
pilha1 = Pilha() 
pilha1.push("va")
pilha1.push("vc")
pilha1.push("vb")
pilha1.push("vy")

#pilha_auxiliar = Pilha()
#pilha3 = Pilha()

print("Tamanho da pilha:", pilha1.size())
print("Elemento do topo:", pilha1.peek())

#print("Desempilhando:", pilha1.pop())
#print("Desempilhando:", pilha1.pop())

print("A pilha está vazia?", pilha1.isEmpty())

#print("Desempilhando:", pilha1.pop())
print("A pilha está vazia?", pilha1.isEmpty())

pilha1.ordenar()
print("Pilha ordenada (original):", pilha1.items)

# Criando uma nova pilha ordenada
pilha1_ordenada = pilha1.ordenar_e_criar_nova()
print("Nova pilha ordenada:", pilha1_ordenada)
print("Pilha original após ordenar:", pilha1.items)