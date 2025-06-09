# 2. Función que indica si un número es par o impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Ejecutar función de par/impar
numero = int(input("pon un número: "))
print(f"El número {numero} es {es_par_o_impar(numero)}.")