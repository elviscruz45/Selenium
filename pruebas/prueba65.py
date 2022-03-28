# this is our descriptor object
class Bar():
    def __init__(self):
        self.value = ''
    def __get__(self, instance, owner):
          print ("returned from descriptor object")
          return self.value
    def __set__(self, instance, value):
          print ("set in descriptor object")
          self.value = value
    def __delete__(self, instance):
          print ("deleted in descriptor objectt")
          del self.value

class Foo():
    bar = Bar()

f = Foo()
#f.bar = 10
print (f.bar)
del f.bar

#set in descriptor object
#returned from descriptor object
#10
#deleted in descriptor object
