#print_args: Función decoradora
def printArgs(func):
  def innerFunc(*args, **kwargs):
    print(args)
    print(kwargs)
    return func(*args, **kwargs)

  return innerFunc

#foobar: Función decorada
@printArgs
def foobar(x, y, z):
  return x * y + z

print(foobar(3, 5, z=10))
# (3, 5)
# {'z': 10}
# 25 = 3 * 5 + 10