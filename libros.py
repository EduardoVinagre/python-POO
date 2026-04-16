from typing import Protocol
from exceptions import LibroNoDisponibleError


class LibroProtocol(Protocol):
    def prestar(self) -> str:
        ...

    def devolver(self) -> str:
        ...

    def calcular_duracion(self) -> str:
        ...

class Libro:
    def __init__(self, titulo: str, autor, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.__veces_prestado = 0

    def __str__(self) -> str:
        return f"{self.titulo} {self.autor} {self.isbn} {self.disponible} Es popular: {self.es_popular()}"

    @classmethod
    def crear_no_disponible(cls, titulo, autor, isbn):
        cls(
            titulo, autor, isbn, disponible=False
        )

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError("El libro no esta disponible")
        self.disponible = False
        self.__veces_prestado += 1
        return f"'{self.titulo}' prestado exitosamente. Prestado {self.__veces_prestado}"
        #return f"'{self.titulo}' no esta disponible"

    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"

    @property
    def es_popular(self):
        if self.__veces_prestado > 5:
            return True
        return False

    @property
    def veces_prestado(self):
        return self.__veces_prestado

    @veces_prestado.setter
    def veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 dias"
    

class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"