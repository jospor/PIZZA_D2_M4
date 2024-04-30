from pizza import Pizza
from tipo_ingrediente import TipoIngrediente

#Mostrar valores de atributos de clase sin crear una instancia
print("Ingredioentes proteicos disponibles: ",TipoIngrediente.ingredientes_proteicos)
print("Ingredientes vegetales disponibles: ",TipoIngrediente.ingredientes_vegetales)
print("tipos de masa disponible: ", TipoIngrediente.tipo_de_masa)

#Verificar presencia de un elemento en una lista usando el método estático
elemento = "salsa de tomate"
lista = ["salsa de tomate", "salsa bbq"]
presente = Pizza.validar_elemento(elemento, lista)
print(f"¿'{elemento}' está en {lista}? {presente}")

#Crear una instancia y solicitar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

#Mostrar los ingredientes y el tipo de masa ingresados, y validar la pizza
print("\nIngredientes de la Pizza:")
print(f"Proteico: {mi_pizza.proteico}")
print(f"Vegetal 1: {mi_pizza.vegetal1}")
print(f"Vegetal 2: {mi_pizza.vegetal2}")
print(f"Masa: {mi_pizza.masa}")
print("¿Es la pizza válida?", "Sí" if mi_pizza.es_valida else "No")

