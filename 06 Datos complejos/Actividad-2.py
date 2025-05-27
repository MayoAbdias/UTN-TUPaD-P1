#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique


#Funcion de fibonacci
def fibonacci(posicion):  
    if posicion == 0:
        return 0            #Caso Base
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2) #Llamada recursiva

num_usuario = int(input("Ingrese el número de la posicion deseada: "))

for i in range(num_usuario +1): #Muestra la serie completa hasta el num ingresado por el usuario.

    print(f"{fibonacci(i)}")