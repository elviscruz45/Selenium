class Vivienda:
	temperatura_maxima = -100 #inicializamos a un valor ficticio muy pequeño

	def __init__(self, temperatura):
		self.temperatura_actual = temperatura


#creamos tres viviendas y registramos su temperatura inicial
v1 = Vivienda(20)

#mostramos la temperatura máxima
print(f'La temperatura máxima es {Vivienda.temperatura_maxima}')


