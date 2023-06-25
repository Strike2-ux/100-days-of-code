def obtener_entrada_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero válido.")


def juego_tablas_de_multiplicar():
    print("Bienvenido al Juego de Tablas de Multiplicar")
    print()
    print("¿Cuánto sabes acerca de las tablas de multiplicar? Elige un número y te daré 10 operaciones para resolver.")
    print()

    familia_de_multiplos = obtener_entrada_entero("Ingresa el número de la tabla: ")
    print()

    contador_correctas = 0
    for i in range(1, 11):
        respuesta_correcta = i * familia_de_multiplos
        print(i, "x", familia_de_multiplos)
        respuesta = obtener_entrada_entero("> ")
        if respuesta == respuesta_correcta:
            print("¡Correcto!")
            contador_correctas += 1
        else:
            print("Eso no es correcto. Debería haber sido", respuesta_correcta)

    if contador_correctas == 10:
        print("¡Wow! ¡Puntuación perfecta! 🥳")
    else:
        print("Obtuviste", contador_correctas, "respuestas correctas de 10.")


if __name__ == "__main__":
    juego_tablas_de_multiplicar()
