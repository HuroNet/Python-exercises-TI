# Invertir palabras en una oración sin invertir
#  las letras de cada palabra.

#     Enunciado: Dada una cadena de caracteres,
#  invierte las palabras sin modificar el orden
#  de las letras dentro de cada palabra.
#     Ejemplo: Entrada: "Hola mundo" -> Salida: "mundo Hola"


def invertir_palabras(palabras):
    # palabras=palabras[::-1]
    invertidas = ""
    for letra in palabras:
        invertidas = letra + invertidas
    return invertidas


# print(invertir_palabras("Hola Mundo"))

# Palindromo
# Enunciado: Verifica si una cadena es la misma al
#  leerla al derecho y al revés, ignorando espacios y mayúsculas.
# Ejemplo: Entrada: "Anita lava la tina" -> Salida: True

def palindromo(palabra):
    inversa= invertir_palabras(palabra).lower().replace(" ","")
    palabra=palabra.replace(" ","").lower()
    print(inversa, palabra)
    if inversa == palabra:
        return True
    else:
        return False
   

print(palindromo("Anita lava la tina"))
