
import requests
import json

def extraer_datos():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()

        # Guardar los datos crudos en un archivo JSON
        with open("datos_crudos.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        print("✅ Extracción completada: datos_crudos.json generado.")
    else:
        print(f"❌ Error al acceder a la API: {response.status_code}")

if __name__ == "__main__":
    extraer_datos()