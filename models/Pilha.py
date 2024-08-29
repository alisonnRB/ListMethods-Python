class Pilha:
    def __init__(self):
        self.lista = []
        self.storage = []

    def insert(self, item):
        self.lista.append(item)

    def next(self):
        if not self.lista:
            return "A pilha está vazia"
        value = self.lista[-1]
        self.storage.append(value)
        del(self.lista[-1])
        return value
    
    def search(self, index):
        if index < 0 or index >= len(self.lista):
            return "Índice fora do intervalo"
        return self.lista[index]
    
    def get_pilha(self):
        return self.lista
    
    def get_storage(self):
         return self.storage