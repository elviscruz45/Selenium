class Tamano():  # Una enumeracion es simplemente ponerle nombre a numeros
    normal = 1
    familiar = 2
    xl = 3


class Pizza:
    def __init__(self, precio, tamano, ingredientes):
        self.precio = precio
        self.tamano = tamano
        self.ingredientes = ingredientes

    @classmethod
    def napolitana(cls, tamano):
        precio_napolitana = 8990 * tamano
        ingredientes = ['Queso', 'Oregano', 'Tomate']
        # Instanciamos 'cls' que es la clase Pizza
        return cls(precio_napolitana, tamano, ingredientes)


    # Puedo crear pizzas 'a mano':
    #hawaiana = Pizza(9990, Tamano.normal, ['Tomate', 'Jamon', 'Pina'])

    # Creamos una pizza con nuestro metodo de clase
print(Pizza.napolitana(Tamano.familiar).ingredientes)