from types import MethodType

class Decorator():

  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Dentro del Decorador.')
    return self.func(*args, **kwargs)

  def __get__(self, instance, cls):
    # Retorna un método si se llama en una instancia
    return self if instance is None else MethodType(self, instance)

class Test():
  @Decorator
  def __init__(self):
    print("Dentro de la función decorada")

a = Test()
# Dentro del Decorador.
# Dentro de la función decorada