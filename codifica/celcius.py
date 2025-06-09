def convertir_celsius_a_fahrenheit(grados_celsius):
    grados_fahrenheit = [(grado * 9/5) + 32 for grado in grados_celsius]
    return grados_fahrenheit

# Ejecutar conversión Celsius → Fahrenheit
grados_celsius = input("ponga los grados Celsius separados por comas: ")
grados_celsius = [float(grado) for grado in grados_celsius.split(",")]
grados_fahrenheit = convertir_celsius_a_fahrenheit(grados_celsius)
print(f"Los grados Fahrenheit son: {grados_fahrenheit}")