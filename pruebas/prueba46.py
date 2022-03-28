from enum import Enum
class Tamano(Enum):  # Una enumeracion es simplemente ponerle nombre a numeros
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


if __name__ == '__main__':
    # Puedo crear pizzas 'a mano':
    hawaiana = Pizza(9990, Tamano.normal, ['Tomate', 'Jamon', 'Pina'])

    # Creamos una pizza con nuestro metodo de clase
    napolitana = Pizza.napolitana(Tamano.familiar)