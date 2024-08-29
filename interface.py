import FilaInterface
import PilhaInterface
import Utilities

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
        response = input("Escolha uma opção: ")
        match response:
            case "1":
                print("Você escolheu Filas")
                FilaInterface.FilaInterface()
            case "2":
                print("Você escolheu Pilhas")
                PilhaInterface.PilhaInterface() 
            case _:
                print("Resposta inválida")
                self.clean.clean(2)
                self.options()  


ListInterfaces()
