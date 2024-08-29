class Fila:
    def __init__(self):
        self.lista = []

    def insert(self, item):
        self.lista.append(item)
        print(f"{item} foi adicionado ao final da fila")

    def next(self):
        if not self.lista:
            return "A fila está vazia"
        value = self.lista[0]
        return value
    
    def search(self, index):
        if index < 0 or index >= len(self.lista):
            return "Índice fora do intervalo"
        return self.lista[index]
    
    def get_fila(self):
        return self.lista