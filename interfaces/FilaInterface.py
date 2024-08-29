from models import Fila
from models import Utilities

class FilaInterface:
    def __init__(self):
        self.fila = Fila.Fila()  
        self.clean = Utilities.Utilities() 
        print("Fila criada")
        self.clean.clean(2)  
        self.options() 

    def options(self):
        print(f"Fila {self.fila.name}: {self.fila.get_fila()}")
        print("Você pode:")
        print("1. Adicionar elemento")
        print("2. Remover e chamar o próximo da fila")
        print("3. Verificar na fila")
        print("4. Ver Histórico")
        print("5. Limpar Fila e voltar ao inicio")
        response = input("Escolha uma opção: ")

        match response:
            case "1":
                value = input("Qual elemento deseja adicionar à fila? ")
                try:
                    self.fila.insert(value) 
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "2":
                try:
                    value = self.fila.next()
                    print(f"{value} é o próximo a ser atendido")
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "3":
                try:
                    index = int(input("Qual índice deseja verificar? "))
                    value = self.fila.search(index)
                    print(f"O item no índice {index} é {value}")
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "4":
                try:
                    value = self.fila.get_storage()
                    print(value)
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()
            
            case "5":
                print(f"A Fila {self.fila.name}: {self.fila.get_fila()} será deletada")
                self.clean.clean(2) 
                print("Retornando ao início...")
                self.clean.clean(2)
                return 

            case _:
                print("Opção inválida")
                self.clean.clean(2)
                self.options()
