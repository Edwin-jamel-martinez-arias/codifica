try:
    # Pide al usuario ingresar un número y multiplicar por dos
    numero = float(input("pon un número: "))
    print(f"El doble del número es: {numero * 2}")

    # Pide un número al usuario entero
    numero_entero = int(input("pon un número entero: "))
except ValueError:
    print("Error: El valor ingresado es incorrecto.")
else:
    print("Número entero ingresado correctamente.")