class Celsius(object):
  def __init__(self, value=0.0): 
    self.value = float(value) 
  def __get__(self, instance, owner): 
    print("Hola")
  def __set__(self, instance, value): 
    self.value = float(value) 
    

class Temperature(object):
      celsius = Celsius()

temp=Temperature()
temp.celsius

#calls Celsius.__get__