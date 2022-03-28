class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute


    @classmethod   
    def tostring(self):
        print('Student Class Attributes: name=',self.name)

std = Student()
std.tostring() 