from tipo_ingrediente import TipoIngrediente

class Pizza:
    def __init__(self):
        self.proteico = ""
        self.vegetal1 = ""
        self.vegetal2 = ""
        self.masa = ""
        self.es_valida = False
        
    @staticmethod
    def validar_elemento(elemento, valores_posibles): #Método estático para validar si un elemento está en la lista de posibles valores.
        return elemento in valores_posibles
    
            
    def realizar_pedido(self):
        #Método para realizar un pedido de pizza interactuando con el usuario.
        self.proteico = input("ingresa el ingrediente proteico (pollo, vacuno, carne vegetal): " )
        self.vegetal1 = input("Ingresa el ingrediente vegetal1 (tomate, aceitunas, champiñones): ")
        self.vegetal2 = input("Ingresa el ingrediente vegetal2 (tomate, aceitunas, champiñones): ")
        self.masa = input("Ingrese el tipo de masa (tradicional, delgada): ")

        
        #Validación de cada uno de los ingredientes y la masa
        self.es_valida = (self.validar_elemento(self.proteico, TipoIngrediente.ingredientes_proteicos) and
                          self.validar_elemento(self.vegetal1, TipoIngrediente.ingredientes_vegetales) and
                          self.validar_elemento(self.vegetal2, TipoIngrediente.ingredientes_vegetales) and
                          self.validar_elemento(self.masa, TipoIngrediente.tipo_de_masa))
        if self.es_valida:
            print("Pedido válido.")
        else:
            print("Pedido inválido.")

