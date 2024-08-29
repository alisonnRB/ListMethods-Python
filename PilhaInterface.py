import Pilha
import Utilities

class PilhaInterface:
    def __init__(self):
        self.pilha = Pilha.Pilha() 
        self.clean = Utilities.Utilities() 
        print("Pilha criada")
        self.clean.clean(2)  
        self.options() 

    def options(self):
        print("Você pode:")
        print("1. Adicionar elemento")
        print("2. Remover e chamar o próximo da pilha")
        print("3. Ver a pilha")
        print("4. Verificar na pilha")
        response = input("Escolha uma opção: ")

        match response:
            case "1":
                value = input("Qual elemento deseja adicionar à pilha? ")
                try:
                    self.pilha.insert(value)  
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "2":
                try:
                    value = self.pilha.next() 
                    print(f"{value} é o próximo a ser atendido")
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "3":
                try:
                    value = self.pilha.get_pilha()  
                    print(value)
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case "4":
                try:
                    index = int(input("Qual índice deseja verificar? ")) 
                    value = self.pilha.search(index)
                    print(f"O item no índice {index} é {value}")
                except Exception as e:
                    print("Algo deu errado:", e)

                self.clean.clean(2)
                self.options()

            case _:
                print("Opção inválida")
                self.clean.clean(2)
                self.options()