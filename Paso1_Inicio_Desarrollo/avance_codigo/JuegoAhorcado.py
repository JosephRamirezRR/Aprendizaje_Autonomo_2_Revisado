# Juego del Ahorcado (avance de código)
#
# Este archivo contiene una primera versión del clásico juego del ahorcado.  Se
# eligió Python por su sintaxis clara y porque permite centrarse en la lógica.
# El objetivo es seleccionar una palabra al azar y permitir que el usuario la
# adivine letra por letra antes de quedarse sin vidas.

import random

def obtener_palabra():
    """
    Selecciona y devuelve una palabra secreta de una lista predefinida.  Todas
    las palabras se almacenan en minúsculas para simplificar las comparaciones.
    """
    palabras = [
        "computadora", "teclado", "pantalla", "guitarra", "celular",
        "hogar", "parangaricutirimicuaro", "lapiz", "botella", "monitor"
    ]
    return random.choice(palabras).lower()

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    """
    Devuelve una cadena que representa el estado actual del tablero.  Por cada
    letra de la palabra secreta se comprueba si ha sido adivinada; si es así,
    se muestra la letra, de lo contrario se coloca un guion bajo.

    :param palabra_secreta: palabra que el usuario intenta adivinar.
    :param letras_adivinadas: conjunto de letras que el usuario ya ingresó.
    :return: representación del tablero como cadena.
    """
    tablero = []
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero.append(letra)
        else:
            tablero.append("_")
    return " ".join(tablero)

def jugar_ahorcado():
    """
    Función principal que ejecuta el juego del ahorcado.  Gestiona las vidas,
    recibe las entradas del usuario y determina si ha ganado o perdido.
    """
    palabra = obtener_palabra()
    letras_adivinadas = set()
    vidas_restantes = 6  # Número de oportunidades del jugador

    while vidas_restantes > 0:
        # Mostrar el tablero actual
        print("\nPalabra:", mostrar_tablero(palabra, letras_adivinadas))
        print("Vidas restantes:", vidas_restantes)

        # Solicitar una letra al usuario
        intento = input("Ingresa una letra: ").lower().strip()

        # Validar que se ingresó una única letra del alfabeto
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor ingresa una sola letra válida.")
            continue

        # Verificar si la letra ya fue ingresada
        if intento in letras_adivinadas:
            print(f"Ya ingresaste la letra '{intento}'. Intenta con otra.")
            continue

        # Registrar la letra ingresada
        letras_adivinadas.add(intento)

        # Comprobar si la letra pertenece a la palabra
        if intento in palabra:
            print("¡Correcto! La letra está en la palabra.")
            # Comprobar si todas las letras han sido adivinadas
            if all(letra in letras_adivinadas for letra in palabra):
                print("\n¡Felicidades! Has adivinado la palabra:", palabra)
                return
        else:
            vidas_restantes -= 1
            print(f"Letra incorrecta. Pierdes una vida.")

    # Si el ciclo termina, el usuario ha perdido
    print("\n¡Has perdido! La palabra secreta era:", palabra)


if __name__ == "__main__":
    jugar_ahorcado()