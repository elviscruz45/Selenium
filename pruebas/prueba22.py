class Vivienda:
    def __init__(self, temperatura,a,b):
        self.temperatura_actual = 10
        self.suma(a,b)
        
    def registrar_temperatura(self, nueva_temperatura):
        self.temperatura_actual=nueva_temperatura+10
        return self.temperatura_actual
    
    def suma(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        return print(c)

casa = Vivienda(20,10,30)
print(casa)