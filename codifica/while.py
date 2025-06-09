contraseña = "secreto"
intento = ""

while intento != contraseña:
    intento = input("pon la contraseña: ")
    if intento != contraseña:
        print("incorrecto.")

print("correcto.")