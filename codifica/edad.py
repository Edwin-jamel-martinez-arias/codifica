# Función qué verifique si es mayor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "es usted mayor de edad."
    else:
        return "aun No eres mayor de edad."
edad = int(input("ponga su edad: "))
print(es_mayor_de_edad(edad))