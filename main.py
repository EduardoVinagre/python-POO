from biblioteca import Biblioteca
from libros import Libro, LibroDigital, LibroFisico
from usuarios import Estudiante, Profesor

mi_libro = Libro(
    "100 años de soledad", "Gabriel Garcia Marquez", "978-8420471839", True
)
otro_libro = LibroFisico("El Principito", "Saint-Exupéry", " 978-6073803762", True)
otro_libro_2 = LibroDigital("El arte de la guerra", "Sun Tzu", " " \
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


estudiante =Estudiante("Luis","1212121","Sistemas")
estudiante_1 =Estudiante("Jose","77520","Salud")
profesor = Profesor("Felipe","2122121")

usuarios = [estudiante, estudiante_1, profesor]

for usuario in usuarios:
    print(usuario.solicitar_libro("Titulo de ejemplo"))

# print(profesor.solicitar_libro("Python básico"))
# print(profesor.solicitar_libro("Python Intermedio"))
# print(profesor.solicitar_libro("Python Avanzado"))
# print(profesor.solicitar_libro("Python / django"))

# print(estudiante.devolver_libro("El arte de la guerra"))
# print(profesor.devolver_libro("El arte de la guerra"))
# print(profesor.devolver_libro("Python básico"))