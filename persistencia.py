import json
from datetime import datetime

class Persistencia:
    def __init__(self, archivo="biblioteca.json") -> None:
        self.archivo = archivo


    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().isoformat()
        }
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)


    def cargar_datos(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        print(f"datos: {datos}")