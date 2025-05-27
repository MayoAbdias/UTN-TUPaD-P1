#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:    #Caso base.
        return n
    else:   #(n%10) me da el ultimo digito y (n // 10) me da el resto de los digitos y asi hasta llegar a un 
            #número menor a 10 que es el caso base.
        return (n % 10) + suma_digitos(n // 10) #Llamada recursiva
    
num_usuario = int(input("Ingrese un número entero positivo: "))

if num_usuario <= 0:
    print("Por favor ingrese un número entero positivo.")
else:
    print(f"La suma de los digitos de {num_usuario} es: {suma_digitos(num_usuario)}")