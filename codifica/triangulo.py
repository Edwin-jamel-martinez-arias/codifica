# 1. Función que retorna el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
# Ejecutar función de triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = calcular_area_triangulo(base, altura)
print(f"El área del triángulo es: {area_triangulo:.2f}")