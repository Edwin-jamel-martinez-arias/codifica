palabras = ["hola", "programación", "python", "lambda", "función", "if", "mundo"]
palabras_extensas = list(filter(lambda x: len(x) >= 5, palabras))
print(palabras_extensas)