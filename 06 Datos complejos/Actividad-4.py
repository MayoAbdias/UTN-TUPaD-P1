#Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto

def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2) #Llamada recursiva: Divide el numero ingresado y va
                                                    #agregando los string ceros y unos de atras hacia adelante.
    
# Pedir al usuario un número
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
