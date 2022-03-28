class Vivienda:
    
	def __init__(self, temperatura):
		self.temperatura_actual = temperatura
		self.registrar_temperatura(temperatura)

	def registrar_temperatura(self, nueva_temperatura):
		self.temperatura_actual=nueva_temperatura+10
		return self.temperatura_actual

casa = Vivienda(20)
print(Vivienda(50).temperatura_actual)