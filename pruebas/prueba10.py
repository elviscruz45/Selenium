
def numero_primos(num):
    
    primos=[]
    cantidad=len(primos)
    contador=0   
    
    for i in range(2,num):
        if i==2:
            primos.append(i)
        else:           
                
            for a in range(2,i):      
                if i%a==0:
                    contador+=1
            if contador==0:
                    primos.append(i)
        contador=0                
    
    print(len(primos))    
    return primos
                
                

print(numero_primos(1000))