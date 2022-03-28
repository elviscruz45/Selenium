class Fraccion:
    def __init__(self, n, d):
        self.numerador = n
        self.denumerador = d
        
    def suma(self):
        self.c=self.numerador+self.denumerador
        return (self.c)
    def resta(self):
        self.restar=self.numerador-self.denumerador
        return (self.c)

f = Fraccion(1, 6)
print(f.suma()) # imprime 1
print(f.resta()) # imprime 1
