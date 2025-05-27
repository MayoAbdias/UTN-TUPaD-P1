#Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛 elevado a (𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1    #Caso base: Todo número elevado a 0 da 1.
    else:
        return base * potencia(base, exponente -1) #Llamada recursiva
    
base = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese el exponente (No negativo): "))

#Verifica que el exponente sea positivo.
if exponente < 0:
    print("El exponente no puede ser negativo.")
else:
    resultado = potencia(base, exponente)    #Guarda el resultado.
    print(f"{base}^{exponente} = {resultado}")


