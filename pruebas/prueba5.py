n = int(input('Give me a number: '))
h = n*n+2 
cousin = []
for x in range(2, h):
    I_think_cousin = True
    
    for divisor in range(2, x):
        if x % divisor == 0:
            I_think_cousin = False
            break

    if I_think_cousin and len(cousin)<n:
        cousin.append(x)

print(cousin)
