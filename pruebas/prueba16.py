class Vivienda:
	temperatura_maxima = -100 #inicializamos a un valor ficticio muy pequeño

	def __init__(self, temperatura):
		self.temperatura_actual = temperatura
		self.registrar_temperatura(temperatura)

	def registrar_temperatura(self, nueva_temperatura):
		self.temperatura_actual = nueva_temperatura
		# si alguna vivienda supera la temperatura máxima se actualiza la variable de clase
		if self.temperatura_actual > self.temperatura_maxima:
			self.__class__.temperatura_maxima = self.temperatura_actual
   

#creamos tres viviendas y registramos su temperatura inicial
v1 = Vivienda(20)
v2 = Vivienda(23)
v3 = Vivienda(18)

#mostramos la temperatura máxima
print(Vivienda.temperatura_maxima)


