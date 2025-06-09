datos = ["m", 3, True, 3.01]

for dato in datos:
    print(f"El dato '{dato}' es de tipo:")
    if dato == "m":
        print("cadena")
    elif dato == 3:
        print("entero")
    elif dato == True:
        print("booleano")
    elif dato == 3.01:
        print("decimal")