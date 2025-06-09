# 3. Función que calcula el área de un círculo
def calcular_area_circulo(radio):
    pi = 3.1416
    area = pi * (radio ** 2)
    return area

# Ejecutar función de área de círculo
radio = float(input("ponga el radio del círculo: "))
area_circulo = calcular_area_circulo(radio)
print(f"El área de su círculo es: {area_circulo:.2f}")