from PIL import Image
import os

# Carpeta de entrada
carpeta_entrada = r'C:\Users\Usuario\Downloads\galeria'

# Obtener el nombre de la marca por consola
marca = input("Introduce el nombre de la marca: ")

# Carpeta de salida para los archivos WebP
carpeta_salida = r'C:\Users\Usuario\Downloads\galeria\galeria_webp'
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Contador para los nombres correlativos
contador = 1

# Obtén la lista de archivos en la carpeta de entrada
archivos = os.listdir(carpeta_entrada)

# Itera sobre los archivos
for archivo in archivos:
    if archivo.endswith('.png'):  # Verifica si el archivo es un PNG
        ruta_entrada = os.path.join(carpeta_entrada, archivo)
        nombre_salida = f'Coches_de_Lujo_{marca}_{contador}.webp'  # Nombre de salida con el nombre de la marca y el contador
        ruta_salida = os.path.join(carpeta_salida, nombre_salida)  # Ruta de salida en la carpeta de salida
        contador += 1

        # Abre la imagen
        imagen = Image.open(ruta_entrada)

        # Guarda la imagen en formato WebP en la carpeta de salida
        imagen.save(ruta_salida, 'WEBP')

print("¡Proceso completado! Las imágenes PNG se han convertido a WebP en la carpeta de salida:", carpeta_salida)
