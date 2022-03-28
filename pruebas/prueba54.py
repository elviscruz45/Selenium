class Decorator:
  """Clase de decorador simple."""
  def __init__(self, a,b):
        self.a = a
        self.b = b
  def suma(self):
    print(self.a+self.b)
    self.c=self.a*self.b
  def resta(self):
        print(self.c)


elvis=Decorator(10,5)
elvis.resta()