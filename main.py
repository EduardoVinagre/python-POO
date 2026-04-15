from typing import Protocol


class LibroProtocol(Protocol):
    def prestar(self) -> str:
        ...

    def devolver(self) -> str:
        ...

    def calcular_duracion(self) -> str:
        ...

class Libro:
    def __init__(self, titulo: str, autor, isbn: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    def __str__(self) -> str:
        return f"{self.titulo} {self.autor} {self.isbn} {self.disponible} Es popular: {self.es_popular()}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.veces_prestado += 1
            return f"'{self.titulo}' prestado exitosamente. Prestado {self.__veces_prestado}"
        return f"'{self.titulo}' no esta disponible"

    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"

    def es_popular(self):
        if self.__veces_prestado > 5:
            return True
        return False

    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 dias"
    

class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"


class Biblioteca:
    def __init__(self, name) -> None:
        self.name = name
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]


mi_libro = Libro(
    "100 años de soledad", "Gabriel Garcia Marquez", "978-8420471839", True
)
otro_libro = Libro("El Principito", "Saint-Exupéry", " 978-6073803762", True)
otro_libro_2 = Libro("El arte de la guerra", "Sun Tzu", " " \
"9798375541266", False)

# print(mi_libro.prestar())
# print(mi_libro.devolver())

# lista_libros = [mi_libro, otro_libro]

# for libro in lista_libros:
#     print(libro)

biblioteca = Biblioteca("")
biblioteca.libros.append(mi_libro)
biblioteca.libros.append(otro_libro)
biblioteca.libros.append(otro_libro_2)

print(biblioteca.libros_disponibles())