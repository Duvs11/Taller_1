#programa para generar un número aleatorio en python

import random

# La funcion input() captura datos desde el teclado
# Como si fuera una cadena de texto (string)

a = input("Limite inferior:")
b = input("Limite superior:")

# Convertir a y b en enteros

a = int(a)
b = int(b)
respuesta = random.randint(a,b)
print(respuesta)