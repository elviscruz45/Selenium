class Decorator:
  """Clase de decorador simple."""
  def __init__(self,casa):
        self.a =print("hola")
        self.b=casa
  def __call__(self):
        print(self.b)

casa=Decorator(211)
casa()