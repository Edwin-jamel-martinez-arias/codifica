try:
    numero = int(input("pon un número entero: "))
except ValueError:
    print("Error: No se pudo convertir a entero.")
else:
    print("Número entero ingresado correctamente.")