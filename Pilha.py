class Pilha:
    def __init__(self):
        self.lista = []

    def insert(self, item):
        self.lista.append(item)

    def next(self):
        if not self.lista:
            return "A pilha está vazia"
        return self.lista[len(self.lista)]
    
    def search(self, index):
        if index < 0 or index >= len(self.lista):
            return "Índice fora do intervalo"
        return self.lista[index]
    
    def get_pilha(self):
        return self.lista