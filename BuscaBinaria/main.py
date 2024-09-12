from models import Utilities
import time

class Main:
    def __init__(self) -> None:
        self.clean = Utilities.Utilities() 
        print("Bem-vindo ao Search do Álison.")
        with open('./palavras/palavras.txt', 'r') as arquivo:
            self.ordenadas = [linha.rstrip() for linha in arquivo]

        self.clean.clean(2)  
        self.inputValue()

    def inputValue(self):
        print("Qual nome deseja procurar nas listas?")
        value = input("")
        inicio = time.perf_counter()
        index = self.search(value)
        fim = time.perf_counter()

        print(f"tempo de execucao é {fim - inicio}")

        if(isinstance(index, int)):
            print(f"A palavra {value} está na posição {index + 1}")
        else:
            print(f"a palavra {value} não está na lista")
        
        self.clean.clean(2)  
        self.inputValue()

    def search(self, value):
        continuar = True
        max = len(self.ordenadas) - 1
        min = 0

        while continuar:
            if(min > max):
                continuar = False
            else:
                index = (max + min ) // 2
                middle_word = self.ordenadas[index]

                if(middle_word == value):
                    return index
                elif(middle_word < value):
                    min = index + 1
                else:
                   max = index - 1

        return "ERRO"
        

if __name__ == "__main__":
    Main()
