from interfaces import FilaInterface
from interfaces import PilhaInterface
from models import Utilities

class ListInterfaces:
    def __init__(self):
        self.clean = Utilities.Utilities()  
        print("Welcome")
        self.clean.clean(2) 
        self.options()

    def options(self):
        print("Com o que vai trabalhar hoje?")
        print("1. Filas")
        print("2. Pilhas")
        print("3. encerrar")
        response = input("Escolha uma opção: ")
        match response:
            case "1":
                print("Você escolheu Filas")
                FilaInterface.FilaInterface()
                self.options()
            case "2":
                print("Você escolheu Pilhas")
                PilhaInterface.PilhaInterface() 
                self.options()

            case "3":
                print("encerrando...")
                self.clean.clean(2) 
                print("Até mais")
                self.clean.clean(2) 
                
            case _:
                print("Resposta inválida")
                self.clean.clean(2)
                self.options()  

if __name__ == "__main__":
    ListInterfaces()
