from models import utilities


class Main:
    def __init__(self) -> None:
        self.clean = utilities.Utilities() 
        print("Bem-vindo ao Search do Álison.")
        with open('./palavras/palavras.txt', 'r') as arquivo:
            self.ordenadas = [linha.rstrip() for linha in arquivo]

        with open('./palavras/palavrasDesord.txt', 'r') as arquivo:
            self.desordenadas = [linha.rstrip() for linha in arquivo]

        self.clean.clean(2)  
        self.inputValue()

    def inputValue(self):
        print("Qual nome deseja procurar nas listas?")
        value = input("")
        self.search(value)

    def search(self, value):

        control1 = False
        control2 = False
 
        for i in range(len(self.ordenadas)):
            if(self.ordenadas[i] == value):
                print(f"O(A) {value} está na posição {i + 1} da lista ordenada")
                control1 = True

        for i in range(len(self.desordenadas)):
            if(self.desordenadas[i] == value):
                print(f"O(A) {value} está na posição {i + 1} da lista desordenadas")
                control2 = True


        if(control2 == False and control1 == False):
            print("Não existe nas listas")
        else:
            if(control1 == False):
                print("Não Existe na lista ordenada")
            if(control2 == False):
                print("Não Existe na lista desordenada")


        self.clean.clean(2)  
        self.inputValue()
        

if __name__ == "__main__":
    Main()
