try:
    # Simula abrir un archivo (ficticio)
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: No hay archivo no existente.")
finally:
    print("Operación finalizada.")