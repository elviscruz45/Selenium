class Animal:
    def nombre(self, animalName):
        print(animalName, 'is an animal.');

# Mammal inherits Animal
class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a mammal.')
        super().nombre(mammalName)

perro=Mammal("perro")