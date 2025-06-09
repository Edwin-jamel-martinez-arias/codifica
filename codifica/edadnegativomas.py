def validar_edad(edad):
    if edad < 0:
        return False
    else:
        return True

# Ejecutar validación de edad
try:
    edad = int(input("ponga su edad: "))
    if validar_edad(edad):
        print(f"La edad {edad} es correcta.")
    else:
        print("La edad no puede ser negativa.")
except ValueError:
    print("Error: Debe ingresar un número entero válido")