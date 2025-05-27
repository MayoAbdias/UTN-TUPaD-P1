#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número

def contar_digitos(numero, digito):
    if numero == 0:
        return 0 #Caso base: No hay mas digitos.
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digitos(numero // 10, digito)# Si el ultimo digito es igual a digito sumamos 1.
    else:
        return contar_digitos(numero // 10, digito) #SiNo seguimos buscando.
    
num_usuario= int(input("Ingrese un número entero positivo: "))
digito_usuario = int(input("Ingrese el digito que desea encontrar y contar: "))

print(f"La cantidad de {digito_usuario} en {num_usuario} es: {contar_digitos(num_usuario, digito_usuario)}")


    
