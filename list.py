import os

# Especifica el directorio que quieres listar
directorio = 'S:\\repositories\\web\\websites\\nomada\\sources\\ds\\images\\bg'

# Lista los archivos en el directorio
archivos = os.listdir(directorio)

# Imprime los archivos
for archivo in archivos:
    print("- " + archivo)