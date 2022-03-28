# this is our descriptor object
class Bar():
    def __init__(self):
        self.value = 'casa'
    def __get__(self):
          print ("returned from descriptor object")
          return self.value
    def __set__(self, value):
          print ("set in descriptor object")
          self.value = value
    def __delete__(self):
          print ("deleted in descriptor objectt")
          del self.value

f=Bar()

#f.bar = 10
del f
print(f)

#set in descriptor object
#returned from descriptor object
#10
#deleted in descriptor object
