def decorator(func):
    print("Decorator")
    return func

@decorator
def Hello():
  print("Hello World")

Hello() 
# [Output]:
# Decorator
# Hello World