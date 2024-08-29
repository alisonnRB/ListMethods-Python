import Fila
import Utilities

class FilaInterface:
    def __init__(self):
        self.fila = Fila.Fila()  
        self.clean = Utilities.Utilities() 
        print("Fila criada")
        self.clean.clean(2)  
        self.options() 

    def options(self):
        print("Você pode:")
        print("1. Adicionar elemento")
        print("2. Remover e chamar o próximo da fila")
        print("3. Ver a fila")
        print("4. Verificar na fila")
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
                    value = self.fila.get_fila()
                    print(value)
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "4":
                try:
                    index = int(input("Qual índice deseja verificar? "))
                    value = self.fila.search(index)
                    print(f"O item no índice {index} é {value}")
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case _:
                print("Opção inválida")
                self.clean.clean(2)
                self.options()
