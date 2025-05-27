#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  # Caso base: 0 o 1 letra es palindromo.
    if palabra[0] != palabra[-1]:
        return False  # Si la primera letra y la ultima son distintas no es palíndromo. Esto lo repite hasta llegar a 1.
    
    #Llamada recursiva sin la primera y ultima letra
    return es_palindromo(palabra[1:-1])

usuario = input("ingrese una palabra sin tilde para confirmar si es palíndromo o no: ").lower()

if es_palindromo(usuario):
    print(f"'{usuario}' es un palíndromo ")
else:
    print(f"'{usuario}' no es un palíndromo")

