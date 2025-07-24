

import shutil
import os

def cargar_datos():
    archivo_origen = "datos_transformados.csv"
    carpeta_destino = "output"
    archivo_destino = os.path.join(carpeta_destino, "datos_finales.csv")

    if not os.path.exists(archivo_origen):
        print("No se encontró el archivo transformado. Ejecuta primero transformacion.py")
        return

    # Crear carpeta de salida si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    # Copiar el archivo transformado al directorio final
    shutil.copyfile(archivo_origen, archivo_destino)
    print(f"Carga completada: archivo final guardado en {archivo_destino}")

if __name__ == "__main__":
    cargar_datos()