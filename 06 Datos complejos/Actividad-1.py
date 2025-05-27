#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario.

#Crea la funcion del factorial.
def factorial_num(num):
    if num == 0 or num == 1: #Caso base.
        return 1
    else:
        return num * factorial_num(num-1)  #Llamada recursiva.
    
num_usuario = int(input("Ingrese un número: "))

#Valido que sea un número positivo.
if num_usuario < 1:
    print("ingrese un número mayor o igual a 1 por favor.")
else:
    print(f"Factoriales desde 1 a {num_usuario}")
    
    for i in range(1, num_usuario +1):
        print(f"{i} = {factorial_num(i)}")